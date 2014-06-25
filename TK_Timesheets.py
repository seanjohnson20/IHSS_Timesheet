#!/usr/bin/env python
from Tkinter import *
import tkMessageBox
import tkFont


app = Tk()
app.title('IHSS Timesheet Calculator')
app.geometry('600x400+400+300')
bckgrnd = 'LightBlue' #'#00ffff'
app.configure(background=bckgrnd)
Hrs = IntVar()
Min = IntVar()
Days = IntVar()
Rad = IntVar()
Rad.set(2)

Filename = StringVar()

Comic = tkFont.Font(family="Comic Sans MS",size=10,weight="bold")
bold = tkFont.Font(weight="bold")


def calc():
    print 'Calculate function is running'
    h = Hrs.get()
    m = Min.get()
    d = Days.get()
    ttl = h * 60 + m
    periods = Rad.get()
    ttlp = ttl/periods
    fName = Filename.get()

    lblspace = Label(text='___________________________',bg=bckgrnd).grid(row=5, column=0, sticky=E)
    lblspace = Label(text='___________________________',bg=bckgrnd).grid(row=5, column=1, sticky=W)

    lbltxtName = Label(text='Filename:',font=Comic,width=20, bg=bckgrnd).grid(row=6, column=0, sticky=E)
    lblvalName = Label(text=fName,bg=bckgrnd).grid(row=6, column=1, sticky=W)

    lbltxtN1 = Label(text='Hrs:Min in Calc:',font=Comic,width=20, bg=bckgrnd).grid(row=7, column=0, sticky=E)
    lblvalN1 = Label(text=str(h)+':'+str(m),bg=bckgrnd).grid(row=7, column=1, sticky=W)

    lbltxtN2 = Label(text='Days in Calc:',font=Comic,width=20, bg=bckgrnd).grid(row=8, column=0, sticky=E)
    lblvalN2 = Label(text=str(d), bg=bckgrnd).grid(row=8, column=1, sticky=W)

    lbltxtRes = Label(text='Total Minutes:',font=Comic,width=20, bg=bckgrnd).grid(row=9, column=0, sticky=E)
    lblvalRes = Label(text=ttl, bg=bckgrnd).grid(row=9, column=1, sticky=W)

    lbltxtRes = Label(text='Number of Periods:',font=Comic,width=20, bg=bckgrnd).grid(row=10, column=0, sticky=E)
    lblvalRes = Label(text=periods, bg=bckgrnd).grid(row=10, column=1, sticky=W)

    lbltxtPer = Label(text='Minutes per period:',font=Comic,width=20, bg=bckgrnd).grid(row=11, column=0, sticky=E)
    lblvalPer = Label(text=str(ttlp), bg=bckgrnd).grid(row=11, column=1, sticky=W)

    tkMessageBox.showinfo('Congratulations', 'Your ' + fName + ' file has been saved.')


Hdr = Label(text='IHSS Timesheet Calculator',font=Comic,bg=bckgrnd).grid(row=0, column=1, sticky=N)

labelNum1 = Label(text='Name of File:',font=Comic,width=20,bg=bckgrnd).grid(row=1, column=0, sticky=E)
entryNum1 = Entry(app, textvariable=Filename, width=20).grid(row=1, column=1, sticky=E)

lblHrsMin = Label(text='Hours:Minutes in Calc:',font=Comic,width=20,bg=bckgrnd).grid(row=2, column=0, sticky=E)
entHrs = Entry(app, textvariable=Hrs,width=20).grid(row=2, column=1, sticky=E)
lblColon = Label(text=':',font=Comic,width=1).grid(row=2, column=2, sticky=W)
entMin = Entry(app, textvariable=Min,width=20).grid(row=2, column=3, sticky=W)

lblDays = Label(text='Days in Calc:',font=Comic, width=20, bg=bckgrnd).grid(row=3, column=0, sticky=E)
entDays = Entry(app, textvariable=Days, width=20).grid(row=3, column=1, sticky=E)

rb1 = Radiobutton(app, text="One period",font=Comic,variable=Rad, value=1, bg=bckgrnd).grid(row=4, column=0, sticky=E)
rb2 = Radiobutton(app, text="Two periods",font=Comic,variable=Rad, value=2, bg=bckgrnd).grid(row=4, column=1, sticky=E)

myButton = Button(app, text='Calculate',font=Comic, width=10, command=calc).place(x=475, y=360)

app.mainloop()

