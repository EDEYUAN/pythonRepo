#!/usr/bin/env python

""" this module is used to ckeck the input string should obey the rule:
     1) begin with alphas or under corss line
     2) follow by the alphas, under corss line or digits
"""

import string
import keyword

alphas = string.letters+'_'
nums = string.digits

print 'Welcome to the Identifier Checker V1.0'

myInput = raw_input('Identifier to test ?')

if myInput in keyword.kwlist:
    print '''It is a keyword !!!
             Don't use it as a indentifier !!!'''
else:
    if len(myInput)>1:
        if myInput[0] not in alphas:
            print ''' Invalid: first symbol must be
                      alphabetic ''' 
        else:
	    for otherChar in myInput[1:]:
	    
                if otherChar not in alphas + nums:
                    print ''' Invalid: remaining 
                              symbols must be alphanumeric '''
                    break
            else:
                print "Okay as an identifier"
    else:
        if myInput[0] not in alphas:
            print ''' Invalid: first symbol must be
                      alphabetic ''' 
        else:    
            print "Okay as an identifier"


 

