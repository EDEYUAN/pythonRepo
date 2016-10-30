#!/usr/bin/env python
# this is the excerise fot chapter 1 for the book core Python programming


'''print '--------------this is answer for 2.2 and 2.3----------'
print 2/3,2.0/3
print 'hello, this is the first time I am using python '
print 1+2*4

print '--------------this is answer for 2-4--------------'
str = raw_input('Plz input a string for this test : ')
print 'The string you have input is:',str

str = raw_input('Plz input a num for this test : ')
print 'The num you have input is:',int(str)




print '--------------this is answer for 2-5--------------'
i = 0
while i<=10:
    print i,
    i = i+1

print ''
for item in range(11):
    print item,

print ''
print '--------------this is answer for 2-6--------------'
inpNum = raw_input('Plz input a num for test case 2-6:')
Num = float(inpNum)
if Num < 0.0:
    print 'You have input a negtive num'
elif Num > 0.0:
    print 'You have input a positive num'
else:
    print 'You have input zero'



print '--------------this is answer for 2-7--------------'
inString = raw_input('Plz input a String for test case 2-7:')
Len = len(inString)
for i in range(Len):
    print inString[i]

print 'Here comes the end for using for structure to ouput each char'

i = 0
while i < Len:
    print inString[i]
    i = i + 1

print 'Here comes the end for using while structure to ouput each char'
'''


print '--------------this is answer for 2-11--------------'
operator = 0
while (operator != 1) and (operator != 2):
    operator = int(raw_input('Plz choose what the operation first,1 for sum;2 for average:'))

    if operator == 1:
        print 'So, you have choose to sum for the num you will input'
    else: 
        if operator == 2:
            print 'So, you have choose to get average for the num you will input'
        else:
            print 'Invalid command !!.Plz try again !!'


print 'Now,Plz input the Num'






















