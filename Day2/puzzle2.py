import csv

with open("input.txt",'rb') as f:
    hash = 0
    for line in f:
        words = line.split()
        for word in words:
            min=max=int(words[0])
            for wordstr in words:
                word=int(wordstr)
                if word>max:
                    max=word
                if word<min:
                    min=word
        hash+=max-min

print hash
            
#    count=0
#    if code[0] == code[-1]:
#        count += int(code[0])
#    for index in range(0,len(code)-1):
#        if code[index]==code[index+1]:
#            count+=int(code[index])
#    print count

