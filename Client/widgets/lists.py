from tkinter import *
from tkinter.messagebox import *
import requests
from json import loads
from .wpersons import PersonWindow
from .quitter import Quitter
from.scrolledList import ScrolledList
from settings import SERVER

class GroupScrolledList(ScrolledList):
    def __init__(self, listbox, elements=None, parent=None, key=('name', ), title=None):
        ScrolledList.__init__(self, elements, parent, key, title)
        self.listboxbind = listbox

    def handleList(self, event):
        label = self.listbox.get(self.listbox.curselection())
        for i in self.elements:
            if i['code'] == label:
                index = i['id']
        r = requests.get('{0}students/{1}'.format(SERVER, index))
        j = (loads(r.text))
        self.runCommand(j)

    def runCommand(self, elements):
        self.listboxbind.fillListbox(elements['persons'])

class StudentScrolledList(ScrolledList):
    def handleList(self, event):
        label = self.listbox.get(self.listbox.curselection())
        for i in self.elements:
            if i['name'] + ' ' + i['surname'] == label:
                person = i
        self.runCommand(person)

    def runCommand(self, person):
        window = Toplevel()
        window.minsize(10, 10)
        window.maxsize(50, 50)
        PersonWindow(person, window)
        Button(window, text='Quit', command=window.destroy, 
            width=10, bg='#bdc3c7', bd=3).pack(side=BOTTOM, anchor=E)

if __name__ == "__main__":
    root = Tk()
    option = [{'name': 'Java'},{'name': 'Python'},{'name': 'C++'}]
    ScrolledList(option, root).pack(side=RIGHT)
    root.mainloop()
    