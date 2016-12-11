from tkinter import *
from tkinter.messagebox import *

class ScrolledList(Frame):
    def __init__(self, elements=None, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets(elements)

    def handleList(self, event):
        label = self.listbox.get(self.listbox.curselection())
        self.runCommand(label)
   
    def makewidgets(self, elements):
        ybar = Scrollbar(self)
        xbar = Scrollbar(self, orient='horizontal')
        list = Listbox(self, relief=SUNKEN)
        ybar.config(command=list.yview)
        xbar.config(command=list.xview)
        list.config(yscrollcommand=ybar.set)
        list.config(xscrollcommand=xbar.set)
        ybar.pack(side=RIGHT, fill=Y)
        xbar.pack(side=BOTTOM, fill=X)
        list.pack(side=LEFT, expand=YES, fill=BOTH)
        list.config(selectmode=BROWSE, setgrid=1)
        list.bind('<Double-1>', self.handleList)
        self.listbox = list
        if elements:
            self.fillListbox(elements)

    def fillListbox(self, elements): 
        self.listbox.delete(0, END)
        for label in elements:
            self.listbox.insert(END, label)

    def runCommand(self, selection):
        showinfo('Selection', selection)

if __name__ == "__main__":
    root = Tk()
    option = ['Java', 'Python', 'C++']
    ScrolledList(option, root).pack(side=RIGHT)
    root.mainloop()
    