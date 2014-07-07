#!/usr/bin/env python
from Tkinter import *
import tkMessageBox
import tkFont
import datetime
import os, sys

# variables
now = datetime.datetime.now()
app = Tk()
app.title('IHSS Timesheet Calculator')
app.geometry('575x400+400+300') # size WxH, position y,x
bckgrnd = 'LightBlue'       #Cyan '#00ffff'
app.configure(background=bckgrnd)
Hrs = IntVar()
Hrs.set(95)
Min = IntVar()
Min.set(56)
Days = IntVar()
Days.set(31)
Rad = IntVar()
Rad.set(2.0)
Filename = StringVar()
Filename.set('Some Month')
myFont = tkFont.Font(family="Comic Sans MS",size=10,weight="bold")
bold = tkFont.Font(weight="bold")
path = os.path.dirname(__file__)

def calc():
    h = Hrs.get()
    m = Min.get()
    d = Days.get()
    ttl_min = h * 60 + m
    periods = Rad.get()
    min_in_period = ttl_min/periods
    fName = Filename.get()

    # prevent crash by testing for divide by zero errors
    if (periods==2 and d<2) or (periods==1 and d<1):
        tkMessageBox.showwarning('Oops', 'Please start over. Your days and periods would cause an error.')
        exit()

    print 'ttl_min: '+str(ttl_min)
    print 'min_in_period: '+str(min_in_period)
    print 'd in period: '+str(d)

    if periods==1:
        print '---------'
        print '1 Period '
        print '---------'
        d_p1=d
        min_in_p1 = min_in_period
        min_per_day_p1 = Integer(min_in_p1/d_p1 + min_in_p1%d_p1)
        print 'min_per_day_p1: ' + str(min_per_day_p1)
        hpd_p1 = int(min_per_day_p1/60)
        mpd_p1 = int(min_per_day_p1%60)
        for i in range(1, d_p1 + 1):
            if min_in_p1 > 2*((hpd_p1*60)+mpd_p1):
                min_in_p1 = min_in_p1 - (hpd_p1*60) - mpd_p1
                print 'Day '+str(i) + ' - ' + str(hpd_p1) + ':' + str('%02d' % mpd_p1)
                print 'Min_in_p1: '+ str(min_in_p1)
            else:
                min_in_p1 = min_in_p1 - (hpd_p1*60) - mpd_p1
                last_min = mpd_p1 + min_in_p1
                if last_min>60:
                    hpd_p1+=1
                    last_min=last_min-60
                print 'Day '+str(i) + ' - ' + str(hpd_p1) + ':' + str('%02d' % (last_min))

    else: # periods==2
        print '---------'
        print '2 Periods'
        print '---------'
        d_p1 = 15
        d_p2 = d - d_p1
        if d < 15:
            d_p1 = d/2
            d_p2 = d - d_p1

        print ' '
        print ' --- Period 1 --- '
        print ' '
        min_in_p1 = min_in_period
        min_per_day_p1 = min_in_p1/d_p1
        print 'min_per_day_p1: ' + str(min_per_day_p1)
        print 'min_in_p1: ' + str(min_in_p1)
        print 'd_p1: ' + str(d_p1)
        hpd_p1 = int(min_per_day_p1/60)
        mpd_p1 = int(min_per_day_p1%60)
        for i in range(1, d_p1 + 1):
            if min_in_p1 > 2 * ((hpd_p1*60)+mpd_p1):
                min_in_p1 = min_in_p1 - (hpd_p1*60) - mpd_p1
                print 'Day '+str(i) + ' - ' + str(hpd_p1) + ':' + str('%02d' % mpd_p1)
                print 'Min_in_p1: '+ str(min_in_p1)
            else:
                print 'ELSE'
                min_in_p1 = min_in_p1 - (hpd_p1*60) - mpd_p1
                last_min = mpd_p1 + min_in_p1
                if last_min>60:
                    hpd_p1+=1
                    last_min=last_min-60
                print 'Day '+str(i) + ' - ' + str(hpd_p1) + ':' + str('%02d' % (last_min))

        print ' '
        print ' -- Period 2 -- '
        print ' '
        min_in_p2 = min_in_period
        min_per_day_p2 = min_in_p2/d_p2
        print 'min_per_day_p2: ' + str(min_per_day_p2)
        print 'min_in_p2: ' + str(min_in_p2)
        print 'd_p2: ' + str(d_p2)
        hpd_p2 = int(min_per_day_p2/60)
        mpd_p2 = int(min_per_day_p2%60)
        for i in range(1, d_p2 + 1):
            if min_in_p2 > 2*((hpd_p2*60)+mpd_p2):
                min_in_p2 = min_in_p2 - (hpd_p2*60) - mpd_p2
                print 'Day '+str(i) + ' - ' + str(hpd_p2) + ':' + str('%02d' % mpd_p2)
                print 'Min_in_p2: '+ str(min_in_p2)
            else:
                print 'ELSE'
                min_in_p2 = min_in_p2 - (hpd_p2*60) - mpd_p2
                last_min = mpd_p2 + min_in_p2
                if last_min>60:
                    hpd_p2+=1
                    last_min=last_min-60
                print 'Day '+str(i) + ' - ' + str(hpd_p2) + ':' + str('%02d' % (last_min))







        # p1=d/periods
        # p2=d-p1
        # print ' '
        # print '--- period 1 ---'
        # print ' '
        # for i in range(1,p1+1):
        #     print 'Day '+str(i)+' - '
        # print ' '
        #
        # print '--- period 2 ---'
        # print ' '
        # for i in range(1,p2+1):
        #     print 'Day '+str(i)+' - '
        # print ' '


    #On screen output
    lblspace = Label(text='_________________',bg=bckgrnd).grid(row=5, column=0, sticky=E)
    lblspace = Label(text='_________________',bg=bckgrnd).grid(row=5, column=1, sticky=W)

    lbltxtName = Label(text='Filename:',font=myFont,bg=bckgrnd).grid(row=6, column=0, sticky=E)
    lblvalName = Label(text=fName,bg=bckgrnd).grid(row=6, column=1, sticky=W)

    lbltxtN1 = Label(text='Hrs:Min in Calc:',font=myFont,bg=bckgrnd).grid(row=7, column=0, sticky=E)
    lblvalN1 = Label(text=str(h)+':'+str(m),bg=bckgrnd).grid(row=7, column=1, sticky=W)

    lbltxtN2 = Label(text='Days in Calc:',font=myFont,bg=bckgrnd).grid(row=8, column=0, sticky=E)
    lblvalN2 = Label(text=str(d), bg=bckgrnd).grid(row=8, column=1, sticky=W)

    lbltxtRes = Label(text='Total Minutes:',font=myFont, bg=bckgrnd).grid(row=9, column=0, sticky=E)
    lblvalRes = Label(text=ttl_min, bg=bckgrnd).grid(row=9, column=1, sticky=W)

    lbltxtRes = Label(text='Number of Periods:',font=myFont,bg=bckgrnd).grid(row=10, column=0, sticky=E)
    lblvalRes = Label(text=periods, bg=bckgrnd).grid(row=10, column=1, sticky=W)

    lbltxtPer = Label(text='Minutes per period:',font=myFont,bg=bckgrnd).grid(row=11, column=0, sticky=E)
    lblvalPer = Label(text=str(min_in_period).format(1.2), bg=bckgrnd).grid(row=11, column=1, sticky=W)

    # alert box
    tkMessageBox.showinfo('Congratulations', 'Your '+fName+' has been saved here : '+str(path)+'/'+str(fName)+'.txt')



Hdr = Label(text='IHSS Timesheet Calculator',font=myFont,bg=bckgrnd).grid(row=0, column=1)

labelNum1 = Label(text='Name of File:',font=myFont,bg=bckgrnd).grid(row=1, column=0, sticky=E)
entryNum1 = Entry(app, textvariable=Filename).grid(row=1, column=1, sticky=E)

lblHrsMin = Label(text='Hours:Minutes in Calc:',font=myFont,bg=bckgrnd).grid(row=2, column=0, sticky=E)
entHrs = Entry(app, textvariable=Hrs).grid(row=2, column=1, sticky=E)
lblColon = Label(text=':',font=myFont,width=1).grid(row=2, column=2, sticky=W)
entMin = Entry(app, textvariable=Min).grid(row=2, column=3, sticky=W)

lblDays = Label(text='Days in Calc:',font=myFont,bg=bckgrnd).grid(row=3, column=0, sticky=E)
entDays = Entry(app, textvariable=Days).grid(row=3, column=1, sticky=E)

rb1 = Radiobutton(app, text="One period",font=myFont,variable=Rad, value=1, bg=bckgrnd).grid(row=4, column=0, sticky=E)
rb2 = Radiobutton(app, text="Two periods",font=myFont,variable=Rad, value=2.0, bg=bckgrnd).grid(row=4, column=1, sticky=E)

myButton = Button(app, text='Calculate',font=myFont, width=10, command=calc).place(x=475, y=360)

app.mainloop()

