#!/urs/bin/env python

'''e5-2_multiply.py --implement the multiply operator for two input'''

import pdb

def Opmultiply(input1,input2):
    # convert the input data format 
    input_data = coerce(input1,input2)
    result = input_data[0]*input_data[1]
    return result




if __name__ == '__main__':
    print 'Test sciptrs for function Opmultiply'
    
    while True: 
        data_s1 = raw_input('Plz input the first data:')
        data_s2 = raw_input('PLz input the second data:')
        try:
            data1 = int(data_s1)
            data2 = int(data_s2)
        except:
            print '***Plz input num'
        else:
            break

    #pdb.set_trace()
    print "The input data : %d %d" % (data1,data2)
    print "The multiply result for input is :%d"% (Opmultiply(data1,data2))




