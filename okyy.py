from tkinter import *
from tkinter.ttk import *
import pickle

root = Tk()

def treeData(event):
    children = tree.get_children()
    print(children)

entry = StringVar()
a = Entry(root, textvariable=entry)
a.grid(column=0,row=0)
#a.bind("<Key>", function)

file_data = []
file = open('data.dat', 'rb')
while True:
    try:
        file_data.append(pickle.load(file))
    except EOFError:
        break
file.close()

column_names = ("Column 1", "Column 2")
tree = Treeview(root, columns=column_names)
tree['show'] = 'headings'
for x in file_data:
    a = tree.insert('', 'end', values=x)
for col in column_names: 
    tree.heading(col, text=col)

tree.grid(column=0, row=1)