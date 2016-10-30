#!/urs/bin/env python

'''e5-17_generateRandomNum.py---generateRandomNum and sort '''

import random as rad


#get the parameter for test
#N -- the number for list element
#M -- the number for chosen element to sort
#n -- the range for list element

#get the Number for list len N
while True:
    radNumForList = raw_input('Plz input a integer for the number of random list:')
    try:
        N = int(radNumForList)
    except:
        print "The number you have input can't be transfer to integer,Plz try again :%s" %radNumForList
    else:
        break

#generate the random num for list
alist = []
for i in range(N):
    ele = rad.random()*(2**31-1)
    alist.append(ele)

#get the number for chosen element
while True:
    choseRadNumForList = raw_input('Plz input a integer for the number for choseing element from the random list:')
    try:
        M = int(choseRadNumForList)
    except:
        print "The number you have input can't be transfer to integer,Plz try again :%s" % choseRadNumForList
    else:
        if M >N :
            print "The number you have input beyond the lenght of the list ,Plz try again.(M=%d,N=%d)" %(M,N)
        else:
            break

#generate the random index for chosen element 
newList = []
for lop in range(M):
    index=rad.randint(0,N)
    newList.append(alist[index])

def ShowListElement(alist,col):
    #show the chosen element 
    for lp in range(M):
        if 0 == (lop % 10):
            print newList[lp]    
	else:    
	    print newList[lp],

ShowListElement(newList,10)
newlist.sort()
ShowListElement(newList,10)


	    

    


