import csv
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
#--------adding word----------------------------------
class demo:
    def data(self):
        wr = open('dictionaryfile.csv', 'a',newline='')
        obj = csv.writer(wr)
        w = self.txt1.get()
        w2 = self.txt2.get()
        if w=='' and w2=='':
            showinfo('my dictionary','Enter both word and meaning correctly')
        else:
            p=[w,w2]
            obj.writerow(p)
            wr.close()
            showinfo('my dictionary','word stored')

    def __init__(self):
        self.root=Tk()
        self.root.geometry('250x250')
        self.lb1=Label(self.root,text='WORD')
        self.lb2=Label(self.root,text='MEANING')
        self.txt1=Entry(self.root)
        self.txt2=Entry(self.root)
        self.bt1=Button(self.root,text='ADD WORD',command=self.data)


        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.txt1.grid(row=0,column=1)
        self.txt2.grid(row=1,column=1)
        self.bt1.grid(row=2,column=1)
        self.root.mainloop()



#-------------------------------------------------------------
obj=demo()
#since all the logic of entering code is in __init__(self), therefore we can call function without using any object
#i.e demo() instead of using obj=demo()



