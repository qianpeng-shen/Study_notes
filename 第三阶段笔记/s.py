from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self,master=None,geometry=None):
        Frame.__init__(self,master,geometry)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alerButton=Button(self,text='Hello',command=self.hello)
        self.alerButton.pack()
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s'%name)
app=Application()
app.master.title('Hello World')
app.master.geometry('800x600')
app.mainloop()

