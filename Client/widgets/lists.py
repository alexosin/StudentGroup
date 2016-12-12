from tkinter import *
from tkinter.messagebox import *
import requests
from json import loads

class ScrolledList(Frame):
    def __init__(self, elements=None, parent=None, key=('name',), title=None):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=YES, padx=20, pady=10)
        self.title = title
        self.elements = elements
        self.key = key
        self.makewidgets()
        
    def handleList(self, event):
        label = self.listbox.get(self.listbox.curselection())
        self.runCommand(label)
   
    def makewidgets(self):
        if self.title:
            Label(self, text=self.title).pack()
        ybar = Scrollbar(self)
        xbar = Scrollbar(self, orient='horizontal')
        list = Listbox(self, relief=SUNKEN)
        ybar.config(command=list.yview)
        xbar.config(command=list.xview)
        list.config(yscrollcommand=ybar.set)
        list.config(xscrollcommand=xbar.set)
        ybar.pack(side=RIGHT, fill=Y)
        xbar.pack(side=BOTTOM, fill=X)
        list.pack(expand=YES, fill=BOTH)
        list.config(selectmode=BROWSE, setgrid=1)
        list.bind('<Double-1>', self.handleList)
        self.listbox = list
        if self.elements:
            self.fillListbox(self.elements)

    def fillListbox(self, elements): 
        self.elements = elements
        self.listbox.delete(0, END)
        for element in elements:
            label = ''
            for i in self.key:
                label += str(element[i]) + ' '
            label = label.rstrip()
            self.listbox.insert(END, label)
    def runCommand(self, selection):
        showinfo('Selection', selection)

class GroupScrolledList(ScrolledList):
    def __init__(self, listbox, elements=None, parent=None, key=('name', ), title=None):
        ScrolledList.__init__(self, elements, parent, key, title)
        self.listboxbind = listbox

    def handleList(self, event):
        label = self.listbox.get(self.listbox.curselection())
        for i in self.elements:
            if i['code'] == label:
                print(i)
                index = i['id']
        r = requests.get('http://localhost:5000/students/' + str(index))
        j = (loads(r.text))
        self.runCommand(j)

    def runCommand(self, elements):
        self.listboxbind.fillListbox(elements['persons'])

class StudentScrolledList(ScrolledList):
    def handleList(self, event):
        label = self.listbox.get(self.listbox.curselection())
        self.runCommand()

    def runCommand(self):
        window = Toplevel()
        window.title

if __name__ == "__main__":
    root = Tk()
    option = [{'name': 'Java'},{'name': 'Python'},{'name': 'C++'}]
    ScrolledList(option, root).pack(side=RIGHT)
    root.mainloop()
    