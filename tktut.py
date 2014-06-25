#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter as tk

root1 = tk.Tk()

label1 = tk.Label(root1, text='value 1')
label2 = tk.Label(root1, text='value 2')

entry1 = tk.Entry(root1)
entry2 = tk.Entry(root1)

button = tk.Button(root1, text='Calculate')

label1.grid(column=0, row=1)
label2.grid(column=0, row=2)

entry1.grid(column=1, row=1)
entry2.grid(column=1, row=2)

button.grid(column=1, row=4)

def doCalc(one, two):
    one = one
    two = two

    ttl = one+two
    print ttl

button.config(command=doCalc)

# Prints the entry text
def showentry(event):
    print(entry.get())
entry1.bind('<Return>', doCalc(entry1.get(),entry2.get()))
entry2.bind('<Return>', doCalc(entry1.get(),entry2.get()))
root1.mainloop()
