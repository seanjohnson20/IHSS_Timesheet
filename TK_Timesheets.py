from Tkinter import *
import tkMessageBox

app=Tk()
app.title('My TK App')
app.geometry('500x400+400+300')
bckgrnd='#00ffff'
app.configure(background=bckgrnd)
Num1=DoubleVar()
Num2=IntVar()
Rad=IntVar()

Filename=StringVar()

def calc():
    print'Calculate function is running'
    valNum1=Num1.get()
    valNum2=Num2.get()
    result=str((valNum1*valNum2)).format(1.2)
    periods=Rad.get()
    valName=Filename.get()

    lblspace=Label(text='__________________',bg=bckgrnd,padx=10).grid(row=5,column=0,sticky=E)
    lblspace=Label(text='__________________',bg=bckgrnd).grid(row=5,column=1,sticky=W)

    lbltxtName=Label(text='Filename:',width=15,bg=bckgrnd,padx=10).grid(row=6,column=0,sticky=E)
    lblvalName=Label(text=valName,bg=bckgrnd).grid(row=6,column=1,sticky=W)

    lbltxtN1=Label(text='Hours in Calc:',width=15,bg=bckgrnd,padx=10).grid(row=7,column=0,sticky=E)
    lblvalN1=Label(text=str(valNum1),bg=bckgrnd).grid(row=7,column=1,sticky=W)

    lbltxtN2=Label(text='Days in Calc:',width=15,bg=bckgrnd,padx=10).grid(row=8,column=0,sticky=E)
    lblvalN2=Label(text=str(valNum2),bg=bckgrnd).grid(row=8,column=1,sticky=W)

    lbltxtRes=Label(text='Equals:',width=15,bg=bckgrnd,padx=10).grid(row=9,column=0,sticky=E)
    lblvalRes=Label(text=result,bg=bckgrnd).grid(row=9,column=1,sticky=W)

    lbltxtPer=Label(text='Periods in Calc:',width=15,bg=bckgrnd,padx=10).grid(row=10,column=0,sticky=E)
    lblvalPer=Label(text=str(periods),bg=bckgrnd).grid(row=10,column=1,sticky=W)

    tkMessageBox.showinfo('Congratulations','Your '+valName+' file has been saved.')

Hdr=Label(text='IHSS Timesheet Calculator',bg=bckgrnd).grid(row=0,column=1,sticky=N)

labelNum1=Label(text='Name of File:',width=15,bg=bckgrnd,padx=10).grid(row=1,column=0,sticky=E)
entryNum1=Entry(app,textvariable=Filename,width=15).grid(row=1,column=1,sticky=W)

labelNum1=Label(text='Hours in Calc:',width=15,bg=bckgrnd,padx=10).grid(row=2,column=0,sticky=E)
entryNum1=Entry(app,textvariable=Num1,width=15).grid(row=2,column=1,sticky=W)

labelNum2=Label(text='Days in Calc:',width=15,bg=bckgrnd,padx=10).grid(row=3,column=0,sticky=E)
entryNum2=Entry(app,textvariable=Num2,width=15).grid(row=3,column=1,sticky=W)

rb1=Radiobutton(app, text="One period", variable=Rad, value=1,bg=bckgrnd,padx=10).grid(row=4,column=0,sticky=E)
rb2=Radiobutton(app, text="Two periods", variable=Rad, value=2,bg=bckgrnd).grid(row=4,column=1,sticky=E)

myButton=Button(app,text='Calculate',width=10,command=calc).place(x=410,y=365)

app.mainloop()

