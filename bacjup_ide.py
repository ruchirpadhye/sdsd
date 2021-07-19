from tkinter import *
import pymysql
from datetime import date,datetime
import os
import subprocess
from tkinter import ttk,filedialog,messagebox
from PIL import Image,ImageTk,ImageDraw,ImageFont
class studio_editor:
    def __init__(self,root):
        self.root=root
        self.true_or_false=False
        self.search_folder_file=StringVar()
        self.xyxyx=StringVar()
        self.root.geometry("1220x700+150+150")
        self.root.resizable(0,0)
        self.root.configure(bg="white")
        self.popup = Menu(root, tearoff=0)
        self.popup.add_command(label="Remove from list")
        Label(self.root,bg="white",text="Studio Editor 2020",font=("arial",23)).place(x=30,y=10)
        Label(self.root,bg="white",text="Open Recent",font=("arial",16)).place(x=30,y=60)
        Label(self.root,bg="black").place(x=667,y=100,width=2,height=500)
        self.button_1=ImageTk.PhotoImage(file="C:\\Users\\sujay\\OneDrive\\Documents\\button1.png")
        self.button_2=ImageTk.PhotoImage(file="C:\\Users\\sujay\\OneDrive\\Documents\\button2.png")
        self.button_3=ImageTk.PhotoImage(file="C:\\Users\\sujay\\OneDrive\\Documents\\button3.png")
        button1=Button(self.root,image=self.button_1,command=self.open_folder_,cursor="hand2")
        button1.place(x=680,y=100,width=510,height=156)
        button2=Button(self.root,image=self.button_2,cursor="hand2")
        button2.place(x=680,y=271,width=510,height=156)
        button3=Button(self.root,image=self.button_3,cursor="hand2")
        button3.place(x=680,y=446,width=510,height=156)
        self.ffff=Frame(self.root,bg="white",bd=0)
        self.ffff.place(x=30,y=100,width=590,height=500)
        self.fffff=Frame(self.root,bg="white",bd=0)
        self.fffff.place(x=620,y=100,width=40,height=500)
        
        self.show_recent_files()
    def remove_shortcut(self,event):
        x, y = b1.winfo_rootx(), b1.winfo_rooty()
        print (x, y)

    def show_real(self):
        print(self.xyxyx.get())
    def detect_right_click(self,event):
        x, y = b1.winfo_rootx(), b1.winfo_rooty()
        print (x, y)
        print(event.y)
        try:
            self.popup.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup.grab_release()
    def show_recent_files(self):
        ins=0
        conn1=pymysql.connect(host="localhost",user="root",password="303303303",database="world")
        cur1=conn1.cursor()
        cur1.execute("select * from folders")

        rowww=cur1.fetchall()
        self.okkk=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\dd.png")
        global b1
        for ijk in rowww:
            
            if str(ijk[4]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]","")=="file":
                font1 = ImageFont.truetype('arial.ttf', size=18)
                font2 = ImageFont.truetype('arial.ttf', size=14)
                image = Image.new('RGB', (580,90), (255, 255, 255))
                draw = ImageDraw.Draw(image)
                im1=Image.open(r"C:\\Users\\sujay\\Downloads\\ssd.jfif")
                im1=im1.resize((80,80),Image.ANTIALIAS)
                draw.text((110,20), str(ijk[1]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]",""), fill=(0,0,0), font=font1,width=8)
                image.paste(im1,(5,5))
                draw.text((110,50), str(ijk[0]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]",""), fill=(0,0,0), font=font2,width=8)
                draw.text((410,30), str(ijk[3]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]",""), fill=(0,0,0), font=font2,width=8)
                draw.text((490,30), str(ijk[2]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]",""), fill=(0,0,0), font=font2,width=8)
                image.save("C:\\Users\\sujay\\OneDrive\\Documents\\buttons\\"+str(ijk[1]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]","")+".jpg")
            else:
                font1 = ImageFont.truetype('arial.ttf', size=18)
                font2 = ImageFont.truetype('arial.ttf', size=14)
                image = Image.new('RGB', (580,90), (255, 255, 255))
                draw = ImageDraw.Draw(image)
                print("done")
                im1=Image.open(r"C:\\Users\\sujay\\Downloads\\ds.png")
                im1=im1.resize((80,80),Image.ANTIALIAS)
                draw.text((110,20), str(ijk[1]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]",""), fill=(0,0,0), font=font1,width=8)
                image.paste(im1,(5,5))
                draw.text((110,50), str(ijk[0]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]",""), fill=(0,0,0), font=font2,width=8)
                draw.text((410,30), str(ijk[3]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]",""), fill=(0,0,0), font=font2,width=8)
                draw.text((490,30), str(ijk[2]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]",""), fill=(0,0,0), font=font2,width=8)
                image.save("C:\\Users\\sujay\\OneDrive\\Documents\\buttons\\"+str(ijk[1]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]","")+".png")
            
        
                
     
        list_files = os.listdir("C:\\Users\\sujay\\OneDrive\\Documents\\buttons")
        print(list_files)
        ins1=0
        if list_files==[]:
            Label(self.ffff,bg="white",text="No Recent Files",font=("arial",20)).pack(anchor="c",pady=200)
        else:
            for path in list_files:
                print(path)
                
                
                if path.endswith(".png"):
                    drink = PhotoImage(file="C:\\Users\\sujay\\OneDrive\\Documents\\buttons\\"+path)
                    b1 = ttk.Button(self.ffff, image=drink,cursor="hand2",command=lambda path=path:self.print_(path), compound="right")
                    b1.pack()
                    l1 = ttk.Label(self.ffff, image=drink)
                    l1.image = drink
                    sdd=Button(self.fffff,image=self.okkk,bd=0,cursor="hand2")
                    sdd.pack()
                    sdd.config(command=lambda path2=path,b=b1,s=sdd:[self.delete_recent_(path2),print(path2),b.destroy(),s.destroy()])
                elif path.endswith(".jpg"):
                    drink = ImageTk.PhotoImage(file="C:\\Users\\sujay\\OneDrive\\Documents\\buttons\\"+path)
                    b1 = ttk.Button(self.ffff, image=drink,cursor="hand2",command=lambda path=path:self.print_(path), compound="right")
                    b1.pack()
                    l1 = ttk.Label(self.ffff, image=drink)
                    l1.image = drink
                    sdd=Button(self.fffff,image=self.okkk,bd=0,cursor="hand2")
                    sdd.pack()
                    sdd.config(command=lambda path2=path,b=b1,s=sdd:[self.delete_recent(path2),b.destroy(),s.destroy()])
                        
                ins+=100
                    
                #ff=Radiobutton(self.ffff,selectcolor="light blue",command=self.show_real,variable=self.xyxyx,background="white",font=("Arial",15),cursor="hand2",image=self.photot,value=str(jjj[1]).replace(",","").replace("(","").replace(")","").replace("[","").replace("'","").replace("]",""),padx=10,indicatoron=0,bd=1,width=14)
                #ff.place(x=0,y=ins,width=580,height=90)
    def after_some_time_home(self):
        self.im7=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\foldername.png")
        self.im8=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\filename.png")
        print(os.path.basename(self.direftory_name))
        d=str(os.path.basename(self.direftory_name.strip(".png").strip(".jpg")))
        
        self.ysb = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.xsb = Scrollbar(self.tree_frame, orient=HORIZONTAL)
        self.tree = ttk.Treeview(self.tree_frame,columns=(""),displaycolumns=(""),yscrollcommand=self.ysb.set,xscrollcommand=self.xsb.set)
        self.ysb.config(command=self.tree.yview)
        self.xsb.config(command=self.tree.xview)
        self.tree.heading('#0', text=d)
        self.tree.column('#0',width=400)
        self.root_node = self.tree.insert('', 'end', text=d,image=self.im7)
        
        self.ltt_t=[]
        self.ltt_t.append(d)
        try:
            import pytesseract
            pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sujay\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
            img=Image.open("C:\\Users\\sujay\\Onedrive\\Documents\\buttons\\"+str(self.direftory_name))
            print(pytesseract.image_to_string(img))
            ddffdd=pytesseract.image_to_string(img)
            xr=list(ddffdd.split("\n"))
            self.direftory_namee=str(xr[1])
            arr=os.listdir(self.direftory_namee)
        except:
         
            conn=pymysql.connect(host="localhost",user="root",password="303303303",database="world")
            cur=conn.cursor()
            listw=list(self.direftory_name.split("."))
            pqr=str(listw[0])
            cur.execute("select Path from folders where Name=%s",pqr)
            row=cur.fetchall()
            self.direftory_namee=str(row[0][0])
            arr=os.listdir(self.direftory_namee)
        for a in arr:
            try:
                if os.path.isdir(self.direftory_namee+"/"+a):
                    print("Folder Name: "+self.direftory_namee+"/"+a)
                    self.l1_node = self.tree.insert(self.root_node, 'end', text=a,image=self.im7)
                    sd=self.direftory_namee+"/"+a
                    self.ltt_t.append(a)
                    brr=os.listdir(sd)
                    for b in brr:
                        if os.path.isdir(sd+"/"+b):
                            print("Folder Name: "+sd+"/"+b)
                            self.l2_node = self.tree.insert(self.l1_node, 'end', text=b,image=self.im7)
                            cd=sd+"/"+b
                            self.ltt_t.append(b)
                            crr=os.listdir(cd)
                            for c in crr:
                                if os.path.isdir(cd+"/"+c):
                                    self.l3_node = self.tree.insert(self.l2_node, 'end', text=c,image=self.im7)
                                    print("Folder Name: "+cd+"/"+c)
                                    dc=cd+"/"+c
                                    self.ltt_t.append(c)
                                    drr=os.listdir(dc)
                                    for d in drr:
                                        if os.path.isdir(dc+"/"+d):
                                            self.l4_node = self.tree.insert(self.l3_node, 'end', text=d,image=self.im7)
                                            print("Folder Name: "+dc+"/"+d)
                                            ed=dc+"/"+d
                                            self.ltt_t.append(d)
                                            err=os.listdir(ed)
                                            for e in err:
                                                if os.path.isdir(ed+"/"+e):
                                                    self.l5_node = self.tree.insert(self.l4_node, 'end', text=e,image=self.im7)
                                                    print("Folder Name: "+ed+"/"+e)
                                                    fd=dc+"/"+d
                                                    self.ltt_t.append(e)
                                                    frr=os.listdir(fd)
                                                    for f in frr:
                                                        if os.path.isdir(fd+"/"+f):
                                                            self.l6_node = self.tree.insert(self.l5_node, 'end', text=f,image=self.im7)
                                                            print("Folder Name: "+fd+"/"+f)
                                                            gd=fd+"/"+f
                                                            self.ltt_t.append(f)
                                                            grr=os.listdir(gd)
                                                            for g in grr:
                                                                if os.path.isdir(gd+"/"+g):
                                                                    self.l7_node = self.tree.insert(self.l6_node, 'end', text=g,image=self.im7)
                                                                    print("Folder Name: "+gd+"/"+g)
                                                                    hd=gd+"/"+g
                                                                    self.ltt_t.append(g)
                                                                    hrr=os.listdir(hd)
                                                                    for h in hrr:
                                                                        if os.path.isdir(hd+"/"+h):
                                                                            self.l8_node = self.tree.insert(self.l7_node, 'end', text=h,image=self.im7)
                                                                            print("Folder Name: "+hd+"/"+h)
                                                                            self.ltt_t.append(h)
                                                                        else:
                                                                            self.l8_node = self.tree.insert(self.l7_node, 'end', text=h,image=self.im8)
                                                                            print("File Name: "+hd+"/"+h)
                                                                else:
                                                                    self.l7_node = self.tree.insert(self.l6_node, 'end', text=g,image=self.im8)
                                                                    print("File Name: "+gd+"/"+g)
                                                        else:
                                                            self.l6_node = self.tree.insert(self.l5_node, 'end', text=f,image=self.im8)
                                                            print("File Name: "+fd+"/"+f)

                                                else:
                                                    self.l5_node = self.tree.insert(self.l4_node, 'end', text=e,image=self.im8)
                                                    print("File Name: "+ed+"/"+e)

                                        else:
                                            self.l4_node = self.tree.insert(self.l3_node, 'end', text=d,image=self.im8)
                                            print("File Name: "+dc+"/"+d)

                                else:
                                    self.l3_node = self.tree.insert(self.l2_node, 'end', text=c,image=self.im8)
                                    print("File Name: "+cd+"/"+c)

                        else:
                            self.l2_node = self.tree.insert(self.l1_node, 'end', text=b,image=self.im8)
                            print("File Name: "+sd+"/"+b)
                else:
                    self.l1_node = self.tree.insert(self.root_node, 'end', text=a,image=self.im8)
                    print("File Name: "+self.direftory_namee+"/"+a)
            except PermissionError as XV:
                print(XV)
                print(self.ltt_t)
        self.xsb.pack(side=BOTTOM,fill=X)
        self.ysb.pack(side=RIGHT,fill=Y)
        self.tree.pack(fill=BOTH,expand=1)
        self.tree.bind("<Button-3>",self.view_all_items_in_tree)
    def after_some_time_refresh(self):
        self.im7=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\foldername.png")
        self.im8=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\filename.png")
        print(os.path.basename(self.direftory_name))
        d=str(os.path.basename(self.direftory_name.strip(".png").strip(".jpg")))
        
        self.ysb = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.xsb = Scrollbar(self.tree_frame, orient=HORIZONTAL)
        self.tree = ttk.Treeview(self.tree_frame,columns=(""),displaycolumns=(""),yscrollcommand=self.ysb.set,xscrollcommand=self.xsb.set)
        self.ysb.config(command=self.tree.yview)
        self.xsb.config(command=self.tree.xview)
        self.tree.heading('#0', text=d)
        self.tree.column('#0',width=400)
        self.root_node = self.tree.insert('', 'end', text=d,image=self.im7)
        
        self.ltt_t=[]
        self.ltt_t.append(d)
        try:
            import pytesseract
            pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sujay\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
            img=Image.open("C:\\Users\\sujay\\Onedrive\\Documents\\buttons\\"+str(self.direftory_name))
            print(pytesseract.image_to_string(img))
            ddffdd=pytesseract.image_to_string(img)
            xr=list(ddffdd.split("\n"))
            self.direftory_namee=str(xr[1])
            arr=os.listdir(self.direftory_namee)
        except:
            
            conn=pymysql.connect(host="localhost",user="root",password="303303303",database="world")
            cur=conn.cursor()
            listw=list(self.direftory_name.split("."))
            pqr=str(listw[0])
            cur.execute("select Path from folders where Name=%s",pqr)
            row=cur.fetchall()
            self.direftory_namee=str(row[0][0])
            arr=os.listdir(self.direftory_namee)
        for a in arr:
            try:
                if os.path.isdir(self.direftory_namee+"/"+a):
                    print("Folder Name: "+self.direftory_namee+"/"+a)
                    self.l1_node = self.tree.insert(self.root_node, 'end', text=a,image=self.im7)
                    sd=self.direftory_namee+"/"+a
                    self.ltt_t.append(a)
                    brr=os.listdir(sd)
                    for b in brr:
                        if os.path.isdir(sd+"/"+b):
                            print("Folder Name: "+sd+"/"+b)
                            self.l2_node = self.tree.insert(self.l1_node, 'end', text=b,image=self.im7)
                            cd=sd+"/"+b
                            self.ltt_t.append(b)
                            crr=os.listdir(cd)
                            for c in crr:
                                if os.path.isdir(cd+"/"+c):
                                    self.l3_node = self.tree.insert(self.l2_node, 'end', text=c,image=self.im7)
                                    print("Folder Name: "+cd+"/"+c)
                                    dc=cd+"/"+c
                                    self.ltt_t.append(c)
                                    drr=os.listdir(dc)
                                    for d in drr:
                                        if os.path.isdir(dc+"/"+d):
                                            self.l4_node = self.tree.insert(self.l3_node, 'end', text=d,image=self.im7)
                                            print("Folder Name: "+dc+"/"+d)
                                            ed=dc+"/"+d
                                            self.ltt_t.append(d)
                                            err=os.listdir(ed)
                                            for e in err:
                                                if os.path.isdir(ed+"/"+e):
                                                    self.l5_node = self.tree.insert(self.l4_node, 'end', text=e,image=self.im7)
                                                    print("Folder Name: "+ed+"/"+e)
                                                    fd=dc+"/"+d
                                                    self.ltt_t.append(e)
                                                    frr=os.listdir(fd)
                                                    for f in frr:
                                                        if os.path.isdir(fd+"/"+f):
                                                            self.l6_node = self.tree.insert(self.l5_node, 'end', text=f,image=self.im7)
                                                            print("Folder Name: "+fd+"/"+f)
                                                            gd=fd+"/"+f
                                                            self.ltt_t.append(f)
                                                            grr=os.listdir(gd)
                                                            for g in grr:
                                                                if os.path.isdir(gd+"/"+g):
                                                                    self.l7_node = self.tree.insert(self.l6_node, 'end', text=g,image=self.im7)
                                                                    print("Folder Name: "+gd+"/"+g)
                                                                    hd=gd+"/"+g
                                                                    self.ltt_t.append(g)
                                                                    hrr=os.listdir(hd)
                                                                    for h in hrr:
                                                                        if os.path.isdir(hd+"/"+h):
                                                                            self.l8_node = self.tree.insert(self.l7_node, 'end', text=h,image=self.im7)
                                                                            print("Folder Name: "+hd+"/"+h)
                                                                            self.ltt_t.append(h)
                                                                        else:
                                                                            self.l8_node = self.tree.insert(self.l7_node, 'end', text=h,image=self.im8)
                                                                            print("File Name: "+hd+"/"+h)
                                                                else:
                                                                    self.l7_node = self.tree.insert(self.l6_node, 'end', text=g,image=self.im8)
                                                                    print("File Name: "+gd+"/"+g)
                                                        else:
                                                            self.l6_node = self.tree.insert(self.l5_node, 'end', text=f,image=self.im8)
                                                            print("File Name: "+fd+"/"+f)

                                                else:
                                                    self.l5_node = self.tree.insert(self.l4_node, 'end', text=e,image=self.im8)
                                                    print("File Name: "+ed+"/"+e)

                                        else:
                                            self.l4_node = self.tree.insert(self.l3_node, 'end', text=d,image=self.im8)
                                            print("File Name: "+dc+"/"+d)

                                else:
                                    self.l3_node = self.tree.insert(self.l2_node, 'end', text=c,image=self.im8)
                                    print("File Name: "+cd+"/"+c)

                        else:
                            self.l2_node = self.tree.insert(self.l1_node, 'end', text=b,image=self.im8)
                            print("File Name: "+sd+"/"+b)
                else:
                    self.l1_node = self.tree.insert(self.root_node, 'end', text=a,image=self.im8)
                    print("File Name: "+self.direftory_namee+"/"+a)
            except PermissionError as XV:
                print(XV)
                print(self.ltt_t)
        self.xsb.pack(side=BOTTOM,fill=X)
        self.ysb.pack(side=RIGHT,fill=Y)
        self.tree.pack(fill=BOTH,expand=1)
        self.tree.bind("<Button-3>",self.view_all_items_in_tree)
    def refresh_content(self):
        
        for i in self.tree_frame.winfo_children():
            i.destroy()
        print(self.direftory_namee)
        self.tree_frame.after("1500",self.after_some_time_refresh)
    
    def home_content(self):
        
        for i in self.tree_frame.winfo_children():
            i.destroy()
        print(self.direftory_namee)
        self.tree_frame.after("1500",self.after_some_time_home)
    def delete_recent(self,which):
        os.remove("C:\\Users\\sujay\\OneDrive\\Documents\\buttons\\"+str(which))
        conn=pymysql.connect(host="localhost",user="root",password="303303303",database="world")
        qr_2=str(which).split(".")
        whichsss=str(qr_2[0])
        cur=conn.cursor()
        cur.execute("delete from folders where Name=%s",(whichsss))
        conn.commit()
    def delete_recent_(self,which1):
        os.remove("C:\\Users\\sujay\\OneDrive\\Documents\\buttons\\"+str(which1))
        qr_2=str(which1).split(".")
        whichs=str(qr_2[0])
        conn=pymysql.connect(host="localhost",user="root",password="303303303",database="world")
        cur=conn.cursor()
        cur.execute("delete from folders where Name=%s",(whichs))
        conn.commit()
    def print_(self,valueis):
        self.direftory_name=valueis
        self.root.withdraw()
        self.open_main_windows()
    def open_folder_(self):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        today = date.today()

# dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        sd=filedialog.askdirectory()
        if sd=="":
            print("d")
        else:
            print(sd)
            conn=pymysql.connect(host="localhost",user="root",password="303303303",database="world")
            cur=conn.cursor()
            fl_name=os.path.basename(sd)
            cur.execute("insert into folders values (%s,%s,%s,%s,%s)",(sd,fl_name,current_time,d1,"folder"))
            conn.commit()
            conn.close()
            qr_code=list(sd.split("/"))
            xsx=str(qr_code[-1])
            self.direftory_name=xsx
            self.root.withdraw()
            self.open_main_windows()
    def in_first(self,*args):
        self.search_entry.config(state=NORMAL)
        self.search_folder_file.set("")
    def out_first(self,*args):
        self.search_entry.config(state="readonly")
        self.search_folder_file.set("Search Solution Explorer - Folder View")
    def hower_1_p1(self,*args):
        self.detroy_b.config(bg="#ffe386")
    def hower_1_m1(self,*args):
        
        self.detroy_b.config(bg="white")
    def hower_1_p(self,*args):
        self.search_b.config(bg="#ffe386")
    def hower_1_m(self,*args):
        
        self.search_b.config(bg="white")
    def view_all_items_in_tree1(self,event,*args):
        donedona=False
        item = self.tree1.identify_row(event.y)
        print("you clicked on", self.tree1.item(item,"text"))
        self.oneoneone=self.tree.item(item,"text")
        self.listz_searchs=[]
        
        try:
            for a in self.all_list_names:
                print("file"+a)
                if str(a).endswith(self.tree1.item(item,"text")):
                    self.listz_searchs.append(a)
                    donedona=True
                    break
            if donedona:
                dscs=self.listz_searchs[0]
                self.dfggfg=dscs
                if os.path.isdir(dscs):
                    self.popup.tk_popup(event.x_root+80, event.y_root, 0)
                else:
                    self.popup1.tk_popup(event.x_root+80, event.y_root, 0)
        finally:
            self.popup.grab_release()
    def search_file_folder_here(self):
        self.listz_searchs=[]
        donedona=False
        self.im77=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\foldername.png")
        self.im88=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\filename.png")
        self.okkkk=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\crossicon.png")
        if self.search_folder_file.get()=="":
            print("empty")
        else:
            for root, dirs, files in os.walk(self.direftory_namee):
                for name in files:
                    if name == self.search_folder_file.get():
                        print (os.path.abspath(os.path.join(root, name)))
                        self.listz_searchs.append(os.path.abspath(os.path.join(root, name)))
                        donedona=True
                    else:
                        for name in dirs:
                            if name == self.search_folder_file.get():
                                print (os.path.abspath(os.path.join(root, name)))
                                self.listz_searchs.append(os.path.abspath(os.path.join(root, name)))
                                donedona=True
                                break
                            
            if donedona:
                dscs=str(self.listz_searchs[0])
                dscsc=dscs
                self.dddd=list(dscs.split("\\"))
                for dddin in self.dddd:
                    if nice_one==dddin:
                        break
                    else:
                        self.dddd.remove(dddin)
            
                self.tree_frame.pack_forget()
                self.tree_frame_over=Frame(self.new_explorer_frame,bg="white",width=400)
                self.tree_frame_over.pack(expand=1,fill=BOTH)
                xcxcxc=str(self.dddd[-1])
                
                #
                if os.path.isdir(dscsc):
                    self.ysb = Scrollbar(self.tree_frame_over, orient=VERTICAL)
                    self.xsb = Scrollbar(self.tree_frame_over, orient=HORIZONTAL)    
                    self.tree1 = ttk.Treeview(self.tree_frame_over,columns=(""),displaycolumns=(""),yscrollcommand=self.ysb.set,xscrollcommand=self.xsb.set)
                    self.ysb.config(command=self.tree1.yview)
                    self.xsb.config(command=self.tree1.xview)
                    self.tree1.heading('#0', text="Search Results")
                    self.tree1.column('#0',width=400)

                    self.root_node1 = self.tree1.insert('', 'end', text=xcxcxc,image=self.im77)
                    arr=os.listdir(dscsc)
                    for a in arr:
                        if os.path.isdir(dscsc+"/"+a):
                            print("Folder Name: "+self.direftory_namee+"/"+a)
                            self.l1_node = self.tree.insert(self.root_node1, 'end', text=a,image=self.im7)
                            sd=self.direftory_namee+"/"+a
                            self.ltt_t.append(a)
                            brr=os.listdir(sd)
                            for b in brr:
                                if os.path.isdir(sd+"/"+b):
                                    print("Folder Name: "+sd+"/"+b)
                                    self.l2_node = self.tree1.insert(self.l1_node, 'end', text=b,image=self.im7)
                                    cd=sd+"/"+b
                                    self.ltt_t.append(b)
                                    crr=os.listdir(cd)
                                    for c in crr:
                                        if os.path.isdir(cd+"/"+c):
                                            self.l3_node = self.tree1.insert(self.l2_node, 'end', text=c,image=self.im7)
                                            print("Folder Name: "+cd+"/"+c)
                                            dc=cd+"/"+c
                                            self.ltt_t.append(c)
                                            drr=os.listdir(dc)
                                            for d in drr:
                                                if os.path.isdir(dc+"/"+d):
                                                    self.l4_node = self.tree1.insert(self.l3_node, 'end', text=d,image=self.im7)
                                                    print("Folder Name: "+dc+"/"+d)
                                                    ed=dc+"/"+d
                                                    self.ltt_t.append(d)
                                                    err=os.listdir(ed)
                                                    for e in err:
                                                        if os.path.isdir(ed+"/"+e):
                                                            self.l5_node = self.tree1.insert(self.l4_node, 'end', text=e,image=self.im7)
                                                            print("Folder Name: "+ed+"/"+e)
                                                            fd=dc+"/"+d
                                                            self.ltt_t.append(e)
                                                            frr=os.listdir(fd)
                                                            for f in frr:
                                                                if os.path.isdir(fd+"/"+f):
                                                                    self.l6_node = self.tree1.insert(self.l5_node, 'end', text=f,image=self.im7)
                                                                    print("Folder Name: "+fd+"/"+f)
                                                                    gd=fd+"/"+f
                                                                    self.ltt_t.append(f)
                                                                    grr=os.listdir(gd)
                                                                    for g in grr:
                                                                        if os.path.isdir(gd+"/"+g):
                                                                            self.l7_node = self.tree1.insert(self.l6_node, 'end', text=g,image=self.im7)
                                                                            print("Folder Name: "+gd+"/"+g)
                                                                            hd=gd+"/"+g
                                                                            self.ltt_t.append(g)
                                                                            hrr=os.listdir(hd)
                                                                            for h in hrr:
                                                                                if os.path.isdir(hd+"/"+h):
                                                                                    self.l8_node = self.tree1.insert(self.l7_node, 'end', text=h,image=self.im7)
                                                                                    print("Folder Name: "+hd+"/"+h)
                                                                                    self.ltt_t.append(h)
                                                                                else:
                                                                                    self.l8_node = self.tree1.insert(self.l7_node, 'end', text=h,image=self.im8)
                                                                                    print("File Name: "+hd+"/"+h)
                                                                        else:
                                                                            self.l7_node = self.tree1.insert(self.l6_node, 'end', text=g,image=self.im8)
                                                                            print("File Name: "+gd+"/"+g)
                                                                else:
                                                                    self.l6_node = self.tree.insert(self.l5_node, 'end', text=f,image=self.im8)
                                                                    print("File Name: "+fd+"/"+f)
                                                                    
                                                        else:
                                                            self.l5_node = self.tree1.insert(self.l4_node, 'end', text=e,image=self.im8)
                                                            print("File Name: "+ed+"/"+e)
                                                            
                                                else:   
                                                    self.l4_node = self.tree1.insert(self.l3_node, 'end', text=d,image=self.im8)
                                                    print("File Name: "+dc+"/"+d)

                                        else:
                                            self.l3_node = self.tree1.insert(self.l2_node, 'end', text=c,image=self.im8)
                                            print("File Name: "+cd+"/"+c)

                                else:
                                    self.l2_node = self.tree1.insert(self.l1_node, 'end', text=b,image=self.im8)
                                    print("File Name: "+sd+"/"+b)
                        else:
                            self.l1_node = self.tree1.insert(self.root_node, 'end', text=a,image=self.im8)
                            print("File Name: "+self.direftory_namee+"/"+a)
                            self.xsb.pack(side=BOTTOM,fill=X)
                            self.ysb.pack(side=RIGHT,fill=Y)
                            self.tree1.pack(fill=BOTH,expand=1)
                            self.tree1.bind("<ButtonRelease-3>",self.view_all_items_in_tree1)

                else:
                    self.ysb = Scrollbar(self.tree_frame_over, orient=VERTICAL)
                    self.xsb = Scrollbar(self.tree_frame_over, orient=HORIZONTAL)    
                    self.tree1 = ttk.Treeview(self.tree_frame_over,columns=(""),displaycolumns=(""),yscrollcommand=self.ysb.set,xscrollcommand=self.xsb.set)
                    self.ysb.config(command=self.tree1.yview)
                    self.xsb.config(command=self.tree1.xview)
                    self.tree1.heading('#0', text="Search Results")
                    self.tree1.column('#0',width=400)

                    self.root_node1 = self.tree1.insert('', 'end', text=xcxcxc,image=self.im88)
                    self.xsb.pack(side=BOTTOM,fill=X)
                    self.ysb.pack(side=RIGHT,fill=Y)
                    self.tree1.pack(fill=BOTH,expand=1)
                    self.tree1.bind("<ButtonRelease-3>",self.view_all_items_in_tree1)
                self.detroy_b=Button(self.new_explorer_frame,image=self.okkkk,command=self.revive_tree_frame,bg="white",bd=0,activeforeground="black",activebackground="#ffe386")
                self.detroy_b.place(x=399,y=53)
                self.detroy_b.bind("<Enter>",self.hower_1_p1)
                self.detroy_b.bind("<Leave>",self.hower_1_m1)
            else:
                messagebox.showerror("Studio Editor","We found no matching items. Please try again.")
   
    def revive_tree_frame(self):
        self.tree_frame_over.destroy()
        self.tree_frame.pack(expand=1,fill=BOTH)
        self.detroy_b.destroy()
    def copy_full_path(self):
        import clipboard
        
        clipboard.copy(self.dfggfg)
    def copy_relative_path(self):
        import clipboard
        
        clipboard.copy(self.oneoneone)
    def open_filder_explorer(self):
        print(self.dfggfg)
        
        self.dfggfg=self.dfggfg.replace("/","\\")
        if os.path.isdir(self.dfggfg):
            subprocess.Popen(f'explorer "{self.dfggfg}"')
        else:
            subprocess.Popen(f'explorer /select,"{self.dfggfg}"')
        
    def view_all_items_in_tree(self,event,*args):
        donedona=False
        item = self.tree.identify_row(event.y)
        print("you clicked on", self.tree.item(item,"text"))
        self.oneoneone=self.tree.item(item,"text")
        self.listz_searchs=[]
        
        try:
            for a in self.all_list_names:
                print("file"+a)
                if str(a).endswith(self.tree.item(item,"text")):
                    self.listz_searchs.append(a)
                    donedona=True
                    break
            if donedona:
                dscs=self.listz_searchs[0]
                self.dfggfg=dscs
                if os.path.isdir(dscs):
                    self.popup.tk_popup(event.x_root+80, event.y_root, 0)
                else:
                    self.popup1.tk_popup(event.x_root+80, event.y_root, 0)
        finally:
            self.popup.grab_release()
    def open_main_windows(self):
        self.original_frame=Toplevel()
        self.original_frame.geometry("1500x800+0+0")
        self.original_frame.minsize(width=1000,height=700)
        self.original_frame.config(bg="#8084c5")
        self.Main_frame_initial=Frame(self.original_frame,bg="#cfd2f8",height=70,bd=2,relief=RIDGE)
        self.Main_frame_initial.pack(side=TOP,fill=X)
        
        self.solution_frame_button_initial=Frame(self.original_frame,bg="#8084c5",width=30,bd=0,relief=RIDGE)
        self.solution_frame_button_initial.pack(side=LEFT,fill=Y,padx=0,pady=5)
        #self.Button_frame_initial=Frame(self.original_frame,bg="black",height=40,bd=2,relief=RIDGE)
        #self.Button_frame_initial.pack(side=TOP,fill=X,padx=5,pady=15)
        self.canvas = Canvas(self.solution_frame_button_initial,height=105,width=20, bg="#8084c5")
        self.canvas.create_text((4, 10), angle="90", anchor="ne", text="Solution Explorer",fill="white")
        self.canvas.bind("<ButtonPress-1>", self.new_explorer)
        self.canvas.place(x=0, y=0 + 10)
      
        self.new_explorer_frame=Frame(self.original_frame,bg="white",bd=0,width=400)
        self.new_explorer_frame.pack(side=LEFT,fill=Y,pady=7,padx=5)
        self.dfff=Frame(self.new_explorer_frame,bg="#ffe386",bd=0,width=400,height=25)
        self.dfff.pack(side=TOP,fill=X)
        Label(self.dfff,bg="#ffe386",text="Solution Explorer - Folder View",font=("arial",11),fg="black").place(x=3,y=0)
        self.function_frame=Frame()
        self.Main_Frame=Frame(self.original_frame,bg="white",height=40,bd=2,relief=RIDGE)
        self.Main_Frame.pack(side=TOP,fill=BOTH,expand=1,padx=7,pady=7)
        self.list_all_impors=Frame(self.new_explorer_frame,bg="#6891d4",bd=0,width=400,height=50)
        self.list_all_impors.pack(side=TOP,fill=X)
        self.im=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\house.png")
        Button(self.list_all_impors,image=self.im,bg="#6891d4",bd=0,activeforeground="black",command=self.home_content,activebackground="#6891d4").place(x=4,y=4)
        self.im1=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\refresh.png")
        Button(self.list_all_impors,image=self.im1,bg="#6891d4",bd=0,activeforeground="black",command=self.refresh_content,activebackground="#6891d4").place(x=29,y=7)
        self.im2=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\collapse.png")
        self.im4=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\newfile.png")
        Button(self.list_all_impors,image=self.im4,bg="#6891d4",bd=0,activeforeground="black",activebackground="#6891d4").place(x=95,y=4)
        self.im5=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\newfolder.png")
        Button(self.list_all_impors,image=self.im5,bg="#6891d4",bd=0,activeforeground="black",activebackground="#6891d4").place(x=120,y=4)
        self.im6=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\search.png")
        self.im7=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\foldername.png")
        self.im8=ImageTk.PhotoImage(file="C:\\Users\\sujay\\Downloads\\filename.png")
        self.search_b=Button(self.list_all_impors,image=self.im6,command=self.search_file_folder_here,bg="white",bd=0,activeforeground="black",activebackground="#ffe386")
        self.search_b.place(x=399,y=28)
        self.search_b.bind("<Enter>",self.hower_1_p)
        self.search_b.bind("<Leave>",self.hower_1_m)
        self.search_entry=Entry(self.list_all_impors,bg="white",state="readonly",textvariable=self.search_folder_file)
        self.search_entry.place(x=1,y=27,width=397,height=21)
        self.search_entry.bind("<FocusIn>",self.in_first)
        self.search_entry.bind("<FocusOut>",self.out_first)
        self.search_folder_file.set("Search Solution Explorer - Folder View")
        self.true_or_false=True
        self.tree_frame=Frame(self.new_explorer_frame,bg="white",width=400)
        self.tree_frame.pack(expand=1,fill=BOTH)
        import os
        print(os.path.basename(self.direftory_name))
        d=str(os.path.basename(self.direftory_name.strip(".png").strip(".jpg")))
        global nice_one
        nice_one=d
        self.ysb = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.xsb = Scrollbar(self.tree_frame, orient=HORIZONTAL)
        self.tree = ttk.Treeview(self.tree_frame,columns=(""),displaycolumns=(""),yscrollcommand=self.ysb.set,xscrollcommand=self.xsb.set)
        self.ysb.config(command=self.tree.yview)
        self.xsb.config(command=self.tree.xview)
        self.tree.heading('#0', text=d)
        self.tree.column('#0',width=400)

        self.root_node = self.tree.insert('', 'end', text=d,image=self.im7)
        
        self.ltt_t=[]
        self.ltt_t.append(d)
        self.all_list_names=[]
        try:
            import pytesseract
            pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sujay\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
            img=Image.open("C:\\Users\\sujay\\Onedrive\\Documents\\buttons\\"+str(self.direftory_name))
            print(pytesseract.image_to_string(img))
            ddffdd=pytesseract.image_to_string(img)
            xr=list(ddffdd.split("\n"))
            self.direftory_namee=str(xr[1])
            print(self.direftory_namee)
            arr=os.listdir(self.direftory_namee)
        except Exception as e:
            print(e)
            conn=pymysql.connect(host="localhost",user="root",password="303303303",database="world")
            cur=conn.cursor()
            listw=list(self.direftory_name.split("."))
            pqr=str(listw[0])
            cur.execute("select Path from folders where Name=%s",pqr)
            row=cur.fetchall()
            self.direftory_namee=str(row[0][0])
            print(self.direftory_namee)
            arr=os.listdir(self.direftory_namee)
        self.all_list_names.append(self.direftory_namee)
        for a in arr:
            try:
                if os.path.isdir(self.direftory_namee+"/"+a):
                    print("Folder Name: "+self.direftory_namee+"/"+a)
                    self.l1_node = self.tree.insert(self.root_node, 'end', text=a,image=self.im7)
                    sd=self.direftory_namee+"/"+a
                    self.ltt_t.append(a)
                    brr=os.listdir(sd)
                    self.all_list_names.append(sd)
                    for b in brr:
                        if os.path.isdir(sd+"/"+b):
                            print("Folder Name: "+sd+"/"+b)
                            self.l2_node = self.tree.insert(self.l1_node, 'end', text=b,image=self.im7)
                            cd=sd+"/"+b
                            self.ltt_t.append(b)
                            crr=os.listdir(cd)
                            self.all_list_names.append(cd)
                            for c in crr:
                                if os.path.isdir(cd+"/"+c):
                                    self.l3_node = self.tree.insert(self.l2_node, 'end', text=c,image=self.im7)
                                    print("Folder Name: "+cd+"/"+c)
                                    dc=cd+"/"+c
                                    self.ltt_t.append(c)
                                    drr=os.listdir(dc)
                                    self.all_list_names.append(dc)
                                    for d in drr:
                                        if os.path.isdir(dc+"/"+d):
                                            self.l4_node = self.tree.insert(self.l3_node, 'end', text=d,image=self.im7)
                                            print("Folder Name: "+dc+"/"+d)
                                            ed=dc+"/"+d
                                            self.ltt_t.append(d)
                                            err=os.listdir(ed)
                                            self.all_list_names.append(ed)
                                            for e in err:
                                                if os.path.isdir(ed+"/"+e):
                                                    self.l5_node = self.tree.insert(self.l4_node, 'end', text=e,image=self.im7)
                                                    print("Folder Name: "+ed+"/"+e)
                                                    fd=dc+"/"+d
                                                    self.ltt_t.append(e)
                                                    frr=os.listdir(fd)
                                                    self.all_list_names.append(fd)
                                                    for f in frr:
                                                        if os.path.isdir(fd+"/"+f):
                                                            self.l6_node = self.tree.insert(self.l5_node, 'end', text=f,image=self.im7)
                                                            print("Folder Name: "+fd+"/"+f)
                                                            gd=fd+"/"+f
                                                            self.ltt_t.append(f)
                                                            grr=os.listdir(gd)
                                                            self.all_list_names.append(gd)
                                                            for g in grr:
                                                                if os.path.isdir(gd+"/"+g):
                                                                    self.l7_node = self.tree.insert(self.l6_node, 'end', text=g,image=self.im7)
                                                                    print("Folder Name: "+gd+"/"+g)
                                                                    hd=gd+"/"+g
                                                                    self.ltt_t.append(g)
                                                                    hrr=os.listdir(hd)
                                                                    self.all_list_names.append(hd)
                                                                    for h in hrr:
                                                                        if os.path.isdir(hd+"/"+h):
                                                                            self.l8_node = self.tree.insert(self.l7_node, 'end', text=h,image=self.im7)
                                                                            print("Folder Name: "+hd+"/"+h)
                                                                            self.ltt_t.append(h)
                                                                            self.all_list_names.append(hd+"/"+h)
                                                                        else:
                                                                            self.l8_node = self.tree.insert(self.l7_node, 'end', text=h,image=self.im8)
                                                                            print("File Name: "+hd+"/"+h)
                                                                            self.all_list_names.append(hd+"/"+h)
                                                                else:
                                                                    self.l7_node = self.tree.insert(self.l6_node, 'end', text=g,image=self.im8)
                                                                    print("File Name: "+gd+"/"+g)
                                                                    self.all_list_names.append(gd+"/"+g)
                                                        else:
                                                            self.l6_node = self.tree.insert(self.l5_node, 'end', text=f,image=self.im8)
                                                            print("File Name: "+fd+"/"+f)
                                                            self.all_list_names.append(fd+"/"+f)

                                                else:
                                                    self.l5_node = self.tree.insert(self.l4_node, 'end', text=e,image=self.im8)
                                                    print("File Name: "+ed+"/"+e)
                                                    self.all_list_names.append(ed+"/"+e)

                                        else:
                                            self.l4_node = self.tree.insert(self.l3_node, 'end', text=d,image=self.im8)
                                            print("File Name: "+dc+"/"+d)
                                            self.all_list_names.append(dc+"/"+d)

                                else:
                                    self.l3_node = self.tree.insert(self.l2_node, 'end', text=c,image=self.im8)
                                    print("File Name: "+cd+"/"+c)
                                    self.all_list_names.append(cd+"/"+c)
                        else:
                            self.l2_node = self.tree.insert(self.l1_node, 'end', text=b,image=self.im8)
                            print("File Name: "+sd+"/"+b)
                            self.all_list_names.append(sd+"/"+b)
                else:
                    self.l1_node = self.tree.insert(self.root_node, 'end', text=a,image=self.im8)
                    print("File Name: "+self.direftory_namee+"/"+a)
                    self.all_list_names.append(self.direftory_namee+"/"+a)
            except PermissionError as XV:
                print(XV)
                print(self.ltt_t)
        self.xsb.pack(side=BOTTOM,fill=X)
        self.ysb.pack(side=RIGHT,fill=Y)
        self.tree.pack(fill=BOTH,expand=1)
        self.tree.bind("<Button-3>",self.view_all_items_in_tree)
        self.popup = Menu(root, tearoff=0)
        self.popup.add_command(label="Add new File") # , command=next) etc...
        self.popup.add_command(label="Add new Folder")
        self.popup.add_separator()
        self.popup.add_command(label="Rename")
        self.popup.add_command(label="Cut")
        self.popup.add_command(label="Paste")
        self.popup.add_command(label="Delete")
        self.popup.add_separator()
        self.popup.add_command(label="Open in File Explorer",command=self.open_filder_explorer)
        self.popup.add_command(label="Copy Path",command=self.copy_full_path)
        self.popup.add_command(label="Copy Relative Path",command=self.copy_relative_path)
        self.popup.add_separator()
        self.popup.add_command(label="View Properties")
        self.popup1 = Menu(root, tearoff=0)
        self.popup1.add_command(label="Open File")
        self.popup1.add_command(label="Run File")
        self.popup1.add_command(label="Debug File")# , command=next) etc...
        self.popup1.add_separator()
        self.popup1.add_command(label="Cut")
        self.popup1.add_command(label="Copy")
        self.popup1.add_command(label="Duplicate")
        self.popup1.add_separator()
        self.popup1.add_command(label="Open in File Explorer",command=self.open_filder_explorer)
        self.popup1.add_command(label="Copy Path",command=self.copy_full_path)
        self.popup1.add_command(label="Copy Relative Path",command=self.copy_relative_path)
        self.popup1.add_separator()
        self.popup1.add_command(label="View Properties")

        Button(self.list_all_impors,image=self.im2,bg="#6891d4",bd=0,activeforeground="black",command=self.collapse_content,activebackground="#6891d4").place(x=45,y=5)
    def new_explorer(self,*args):
        
        if self.true_or_false==True:
            self.new_explorer_frame.pack_forget()
            self.true_or_false=False
            self.Main_Frame.pack_forget()
            self.Main_Frame.pack(side=TOP,fill=BOTH,expand=1,padx=7,pady=7)
        else:
            self.new_explorer_frame.pack(side=LEFT,fill=Y,pady=7,padx=5)
            self.Main_Frame.pack_forget()
            self.Main_Frame.pack(side=TOP,fill=BOTH,expand=1,padx=7,pady=7)
            self.true_or_false=True
            #self.Button_frame_initial.pack_forget()
            #self.Button_frame_initial.pack(side=TOP,fill=X,padx=5,pady=15)
            
    def collapse_content(self):
        
        self.tree.item(self.l1_node,open=False)    
        self.tree.item(self.root_node,open=False)

root=Tk()
ob=studio_editor(root)
root.mainloop()