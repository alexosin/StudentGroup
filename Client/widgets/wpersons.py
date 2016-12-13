from tkinter import *
import tkinter.messagebox as messagebox
import requests
from json import loads
from widgets.scrolledList import ScrolledList 

class PersonWindow(Frame):
    def __init__(self, person, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack(expand=YES, fill=BOTH)
        self.person = person
        self.makeRequest()
        firstrow = Frame(self)
        firstrow.pack(side=TOP, expand=YES, fill=BOTH)
        box = Frame(firstrow, relief=RIDGE, bd=5)
        box.pack(side=LEFT,anchor=NW, expand=YES, fill=X)
        self.makeform(box, person, ['Name', 'Surname', 'Patronymic', 
            'Birth Date',  'Birth Place', 'Telephone', 'Address'], 
            title='Personal Information')
        self.personal = box
        box = Frame(firstrow, relief=RIDGE, bd=5, width=self.personal['width'])
        box.pack(side=LEFT, anchor=N, expand=YES, fill=X)
        self.makeform(box, self.contract, ['Number', 'Book Number', 
            'Date', 'Kind'], title='Contract information')
        self.contract = box
        self.bcalc = Button(self.personal, text='Calculate average mark', 
            command=self.calc, bd=4, bg='#bdc3c7')
        self.bcalc.pack(side=RIGHT, expand=YES, fill=X)

        secondrow = Frame(self)
        secondrow.pack(side=TOP, expand=YES, fill=BOTH)
        ScrolledList(elements=self.violations, parent=secondrow, 
            title='Violations', key=('order_kind', 'punish_kind', 
            'violation_kind', 'order_date', 'order_number', 'order_text'))

    def makeRequest(self):
        index = self.person['id']
        try:
            r = requests.get('http://localhost:5000/contract/' + str(index))
            contract = loads(r.text)
            r = requests.get('http://localhost:5000/marks/' + str(index))
            marks = loads(r.text)
            r = requests.get('http://localhost:5000/violations/' + str(index))
            violations = loads(r.text)
        except Exception as e:
            messagebox.showerror(message=e)
        self.contract = contract['contract']
        self.marks = marks['marks']
        self.violations = violations['violations']

    def makeform(self, root, source, fields, title):
        Label(root, text=title, anchor='w', width=15).pack()
        for field in fields:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            f = field.lower()
            f = f.replace(' ', '_')
            ent.insert(0, source[f] or 'Unknown')
            row.pack(side=TOP, padx=1, pady=1)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=BOTH)
    
    def calc(self):
        text = 'Average mark = '
        self.bcalc['text'] = text + str(sum(self.marks)/len(self.marks))

if __name__=='__main__':
    person = {'name': 'Alex'}
    PersonWindow(person).mainloop()
