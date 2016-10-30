#!/usr/bin/env python

'readTextFile.py -- read and display text file'


import os
import string



#get filename
fname = raw_input('Enter file name :')
print 



#attempt to open file for reading

try:
    fobj = open(fname,'r')
except IOError,e:
    print "*** file open error:",e
else:
    #display contents for the screen
    for eachline in fobj:
        print string.strip(eachline)
    fobj.close()


print 

#print tip for reading done
print '***Reading Done***'

