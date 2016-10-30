#!/usr/bin/env python

'readNwriteTextFile.py -- create or read a text file'

import os
import string

def createfunc():
	ls = os.linesep
	
	#get the file name for create
	while True:
            fname = raw_input('Enter a filename: ')
	    if os.path.exists(fname):
	        print "The file '%s' already exists" %fname
	    else:
		break
	#get the text 
	all = []
	print "\nEnter the content for this file,('.'for quit input)\n"
	while True:
	    entry = raw_input(">>")
	    if entry == '.':
	        break
	    else:
		all.append(entry)
	
	#write the text into the file
	fobj = open(fname,'w')
	for x in all:
            #fobj.write(['%s%s' % (x,ls)]) #it seems can't work well in OS win7
	    fobj.write(x+ls)
	fobj.close()

	print "\nWrite File Done\n"


def readfunc():

	#get the file name for read
        fname = raw_input('Enter a filename: ')
	print
	
	#try to read the file with the specific name
	try:
	    fobj = open(fname,'r')
	except IOError,e:
	    print "***IOError %s" %e
	else:
	#print the content on the screen
	    for eachline in fobj:
	        print string.strip(eachline)
	    fobj.close()
	print "\nRead file Done\n"



if __name__ == '__main__':
     #get the operation instructor for text file
     while True:
         op = int(raw_input('Chose the operation, 0 for create and 1 for read:'))
	 if op != 1 and op != 0:
             print "***Invalid operation instruct input: %d" %op
	 else:
             break
     #get operation
     if op == 0:
         createfunc()
     else:
         readfunc()


