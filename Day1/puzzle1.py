import csv

with open("input.txt",'rb') as f:
    for line in f:
        code = line
    count=0
    if code[0] == code[-1]:
        count += int(code[0])
    for index in range(0,len(code)-1):
        if code[index]==code[index+1]:
            count+=int(code[index])
    print count