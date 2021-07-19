
from pygments import lex
from pygments.lexers.python import PythonLexer as Lexer
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from pygments.token import Generic
from pygments.lexer import bygroups
from pygments.styles import get_style_by_name
class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget
        
    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)
class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or 
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result   
class Example(tk.Frame):
    def __init__(self,master, *args, **kwargs):
        
        tk.Frame.__init__(self, *args, **kwargs)
        
        self.text = CustomText(self,bg="black",undo=True,insertbackground="white",font=("arial",13),fg="white")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Arial", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)


        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)
        #self.highlighter = Highlighter(self.text, 'C:/Users/91996/Documents/Visual studio code/python.yaml')
        
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        self.text.bind("<Control-f>", self.show_find)
        self.text.bind('<Control-a>', self.select_all)
        #self.text.bind('<Control-c>', self.copy)
        #self.text.bind('<Control-v>', self.paste)
        #self.text.bind('<Control-x>', self.cut)
        #self.text.bind('<Control-y>', self.text.edit_undo)
        #self.text.bind('<Control-z>', self.text.edit_redo)
        self.lexer = Lexer()
        self.syntax_highlighting_tags = self.load_style("monokai")
        self.text.bind("<KeyRelease>", lambda event: self.check_markdown())
        
        self.text.bind("<<TextModified>>", self.onModification)
        self.text.bind('<KeyRelease-parenleft>', lambda x : self.autocomplete('('))
        self.text.bind('<KeyRelease-braceleft>', lambda x : self.autocomplete('{'))
        self.text.bind('<KeyRelease-bracketleft>', lambda x : self.autocomplete('['))
        #self.text.bind('<KeyRelease-colon>', lambda x : self.autocomplete(':'))
        self.text.bind('<KeyRelease-quoteright>', lambda x : self.autocomplete('\''))
        self.text.bind('<KeyRelease-quotedbl>', lambda x : self.autocomplete('\"'))
    def load_style(self,stylename):
        style = get_style_by_name(stylename)
        syntax_highlighting_tags = []
        for token, opts in style.list_styles():
            kwargs = {}
            fg = opts['color']
            bg = opts['bgcolor']
            if fg:
                kwargs['foreground'] = '#' + fg
            if bg:
                kwargs['background'] = '#' + bg
            font = ('Monospace', 10) + tuple(key for key in ('bold', 'italic') if opts[key])
            kwargs['font'] = font
            kwargs['underline'] = opts['underline']
            self.text.tag_configure(str(token), **kwargs)
            syntax_highlighting_tags.append(str(token))
        self.text.configure(bg=style.background_color,
                         fg=self.text.tag_cget("Token.Text", "foreground"),
                         selectbackground=style.highlight_color)
        self.text.tag_configure(str(Generic.StrongEmph), font=('Monospace', 10, 'bold', 'italic'))
        syntax_highlighting_tags.append(str(Generic.StrongEmph))
        return syntax_highlighting_tags   

    def check_markdown(self,start='insert linestart', end='insert lineend'):
        data = self.text.get(start, end)
        while data and data[0] == '\n':
            start = self.text.index('%s+1c' % start)
            data = data[1:]
        self.text.mark_set('range_start', start)
        # clear tags
        for t in self.syntax_highlighting_tags:
            self.text.tag_remove(t, start, "range_start +%ic" % len(data))
        # parse text
        for token, content in lex(data, self.lexer):
            self.text.mark_set("range_end", "range_start + %ic" % len(content))
            for t in token.split():
                self.text.tag_add(str(t), "range_start", "range_end")
            self.text.mark_set("range_start", "range_end")

       
    def cut(self, event=None):
        self.text.event_generate("<<Cut>>")

    def copy(self, event=None):
        self.text.event_generate("<<Copy>>")

    def paste(self, event=None):
        self.text.event_generate("<<Paste>>")

    
    def select_all(self, event=None):
        self.text.tag_add("sel", 1.0, tk.END)

        return "break"

    def replace_text(self):
        if self.find_match_index:

            end = f"{self.find_match_index}+{len(self.text_to_find_what.get())}c"
            self.text.replace(self.find_match_index, end, self.text_to_replace_what.get())

            self.find_search_starting_index = f"{self.find_match_index} linestart"
            self.find_match_index = None
    def find_word(self):
        self.find_match_index = None
        
        length = tk.IntVar()
        idx = self.text.search(self.text_to_find_what.get(), self.find_search_starting_index, stopindex=tk.END, count=length)
        if idx:
            self.text.tag_remove('find_match', 1.0, tk.END)

            end = f'{idx}+{length.get()}c'
            self.text.tag_add('find_match', idx, end)
            self.text.see(idx)

            self.find_search_starting_index = end
            self.find_match_index = idx
        else:
            if self.find_match_index!=1.0:
                if msg.askyesno("No more results", "No further matches. Repeat from the beginning?"):
                    self.find_search_starting_index = 1.0
                    self.find_match_index = None
                    self.find_word()
            else:
                msg.showinfo("No Matches", "No matching text found.")

    def show_find(self,event):
        self.find_window_what=tk.Toplevel(self)
        self.find_window_what.geometry('360x105')
        self.find_window_what.title('Find And Replace')
        self.find_window_what.resizable(0,0)
        self.find_window_what.focus_force()
        self.find_window_what.grab_set()
        self.text.tag_configure('find_match', background="yellow")
        
        self.text_to_find_what=tk.StringVar()
        self.text_to_replace_what=tk.StringVar()
        top_frame = tk.Frame(self.find_window_what,bg="white")
        middle_frame = tk.Frame(self.find_window_what,bg="white",bd=2)
        bottom_frame = tk.Frame(self.find_window_what,bg="white")
        find_entry_label = tk.Label(top_frame, text="Find:",bg="white",font=("arial",10))
        self.find_entry = ttk.Entry(top_frame, textvar=self.text_to_find_what)
        self.find_search_starting_index = 1.0
        replace_entry_label = tk.Label(middle_frame, text="Replace:",font=("arial",10),bg="white")
        self.replace_entry = ttk.Entry(middle_frame, textvar=self.text_to_replace_what)

        self.find_button = ttk.Button(bottom_frame,command=self.find_word, text="Find Next")
        self.replace_button = ttk.Button(bottom_frame, text="Replace ",command=self.replace_text)
        self.match_button = ttk.Button(bottom_frame, text="Match Case")
    
        self.cancel_button = ttk.Button(bottom_frame, text="Cancel")

        find_entry_label.place(x=2,y=4)
        self.find_entry.place(x=62,y=4,width=292)

        replace_entry_label.place(x=0,y=4)
        self.replace_entry.place(x=60,y=4,width=292)

        self.find_button.place(x=5,y=8,width=80)
        self.replace_button.place(x=95,y=8,width=80)
        self.cancel_button.place(x=275,y=8,width=80)
        self.match_button.place(x=185,y=8,width=80)
        
        top_frame.place(x=0,y=0,width=360,height=30)
        middle_frame.place(x=0,y=30,width=360,height=30)
        bottom_frame.place(x=0,y=60,width=360,height=55)

    def autocomplete(self, val) :
        if val == '(' :
            self.text.insert(tk.INSERT, ')')
        elif val == '{' :
            self.text.insert(tk.INSERT, '}')
        elif val == '[' :
            self.text.insert(tk.INSERT, ']')
        elif val == '\'' :
            self.text.insert(tk.INSERT, '\'')
            self.text.mark_set('sentinel', str(float(self.text.index(tk.INSERT))))
        elif val == '\"' :
            self.text.insert(tk.INSERT, '\"')
            self.text.mark_set('sentinel', str(float(self.text.index(tk.INSERT))))
        elif val == ':' :
            text = self.text.get(1.0, tk.INSERT).strip().replace(' ', '')
            if text[(text.index(':') - 1) : text.index(':')] == ')' :
                self.text.insert(tk.INSERT, '\n')
                self.text.insert(tk.INSERT, '\t')
            else:
                self.text.insert(tk.INSERT, '\n')
                self.text.insert(tk.INSERT, '\t')
        return
    def onModification(self,*args):
        print(self.text.get('1.0',"end").strip("\\n"))
        print("ok")
        if self.text.get('1.0',tk.END).strip("\\n"):
            pass
    def _on_change(self, event):
        self.linenumbers.redraw()
if __name__ == '__main__':
    root = tk.Tk()
    frame1=tk.Frame(root)
    frame1.pack(fill=tk.BOTH,expand=1)
    Example(frame1).pack(side="top", fill="both", expand=True)
    root.mainloop()
     