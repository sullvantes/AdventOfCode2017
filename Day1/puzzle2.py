import csv

with open("input.txt",'rb') as f:
    for line in f:
        code = line
#code = "123123"
    comparison_index = len(code)/2
    print comparison_index
    count=0
    #if code[0] == code[-1]:
    #    count += int(code[0])
    for index in range(0,len(code)):
        if (index+comparison_index) > (len(code)-1):
            if code[index]==code[index+comparison_index-len(code)]:
                count+=int(code[index])
            print index , index+comparison_index-len(code)
        else:        
            if code[index]==code[index+comparison_index]:
                count+=int(code[index])
            print index, index+comparison_index
    print count