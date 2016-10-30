#!/urs/env/bin python

'''e5-3_get_score.py --ouput the grade for input num'''

def get_grade(num):
    if (num>100) or (num < 0):
        return 'Error'
    elif 90<=num<=100:
        return 'A'
    elif 80<=num<=89:
        return 'B'
    elif 70<=num<=79:
        return 'C'
    elif 60<=num<=69:
        return 'D'
    else:
        return 'F'


if __name__ == '__main__':
    #get the input score
    while True:
        num_input = raw_input('Plz input a num for this test:')
        try:
            num = int(num_input)
        except:
            print 'Plz input a num,try again'
        else:
            break
    #cal the function
    grade_return = get_grade(num)
    if grade_return == 'Error':
        print 'The num you have input is not bigger than 0 and little than 100' 
    else:    
        print "The grade for input num is %s" % grade_return



   
    
