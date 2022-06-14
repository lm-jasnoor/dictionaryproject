import csv
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
class demo:

# -----------------searching word----------------------------
    def search(self):
            w3 = self.txt3.get()
            w4 = w3.lower()
            rd2 = open('dictionaryfile.csv', 'r')
            obj2 = csv.reader(rd2)
            self.t1.delete(*self.t1.get_children())
            i=0
            for r in obj2:
                if w4 in r[0]:
                    self.t1.insert('', index=i, values=(r[0], r[1]))
                    i=i+1

#window2----------------------------------------------------------------------
    def __init__(self):
        self.root=Tk()

        self.p1=PanedWindow(self.root)
        self.p2=PanedWindow(self.root)

        self.lb3=Label(self.p1,text='SEARCH')
        self.txt3=Entry(self.p1)
        self.bt2=Button(self.p1,text='SEARCH',command=self.search)


        self.t1 = Treeview(self.p2, columns=('word', 'meaning'))
        self.t1.column('word', width=100)
        self.t1.column('meaning', width=1200)
        self.t1.heading('word', text='WORD')
        self.t1.heading('meaning', text='MEANING')
        self.t1['show'] = 'headings'

        rd = open('dictionaryfile.csv', 'r')
        obj = csv.reader(rd)
        i = 0
        for l in obj:
            self.t1.insert('', index=i, values=l)
            i = i + 1


        self.lb3.grid(row=0, column=0)
        self.txt3.grid(row=0, column=1)
        self.bt2.grid(row=0, column=2)
        self.t1.pack()


        self.p1.pack()
        self.p2.pack()

        self.root.mainloop()
obj=demo()

