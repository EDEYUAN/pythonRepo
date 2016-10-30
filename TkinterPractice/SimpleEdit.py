#/usr/bin/python


import sys
import os
import tkFileDialog
from Tkinter import *


class Note():

    def __init__(self):
        self.tk = Tk()
	self.createUI()
	self.tk.mainloop()


    def createUI(self):
        #ceate menu
	menubar = Menu(self.tk)
	fmenu = Menu(menubar,tearoff = 0)
	fmenu.add_command(label = 'Open',command = self.open)
	fmenu.add_command(label = 'Save',command = self.save)
	fmenu.add_command(label = 'Exit',command = exit)
	menubar.add_cascade(label = "File",menu = fmenu)
	self.tk.config(menu = menubar)
	self.text = Text()
	self.text.pack()

    def save(self):
        txtContent = self.text.get(1,0,END)
        self.saveFile(content = txtContent)

    def open(self):
        self.filename = tkFileDialog.askopenfilename(initialdir = os.getcwd())
        filecontent = self.openFile(fname = self.filename)
        if filecontent is not -1:
            self.text.delete(1,0,END)
	    self.text.insert(1,0,filecontent)



    '''
       The filename is file name + full path
    '''
    def openFile(self,fname = None):
        if name is None:
            return -1
        self.fname = fname
        file = open(fname,'r+')
        content = file,read()
        file.close()
        return content

    def saveFile(self,content = None):
        if content is None:
            return -1
        file = open(self.fname,'w')
        file.write(content)
        file.flush()
        file.close()
        return 0 

    def exit(self):
        sys.exit(0)



if __name__ == '__main__':
    Note()












         







