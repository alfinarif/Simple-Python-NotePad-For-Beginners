from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry('500x600')
root.title('NotePad')
root.iconbitmap('logo.ico')
## functions area
def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if open_file is None:
        return
    text = str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()
def open_file():
    file = filedialog.askopenfile(mode='r',filetype=[('text file','*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)   
def clear():
    entry.delete(1.0,END)
btn1 = Button(root,text='Save File',command=save_file)
btn1.place(x=10,y=10)

btn2 = Button(root,text='Open File',command=open_file)
btn2.place(x=70,y=10)

btn3 = Button(root,text='Clear Text',command=clear)
btn3.place(x=135,y=10)

entry = Text(root,height=33,width=58,wrap=WORD)
entry.place(x=10,y=50)
entry.focus_set()
root.mainloop()