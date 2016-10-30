#!/usr/bin/env/python

''' this module aim to use Tkinter module to generate a GUI
'''

from Tkinter import *
#def a function to resize the words according to the scale of the slice 
def resize(ev=None):
    label.config(font='Helvetica -%d bold' %scale.get())

# the main gui
top = Tk()
# set the size for main window 
top.geometry('600x400')
# create a Label object with specfic attributes 
label = Label(top,text = 'hello world!',font = 'Helvetica -12 bold')
label.pack(fill = Y,expand = 1)

# create a Scale object with specific attributes and register the command fuction
scale = Scale(top,from_=10,to = 40,orient = HORIZONTAL, command = resize)
# set the initial value and position for scale
scale.set(12)
scale.pack(fill = X, expand = 1)
# create a Button obj with specific attributes and register the command function
quit = Button(top, text = 'Quit',command = top.quit,activeforeground = 'white', activebackground = 'red')

quit.pack()
mainloop()







