import csv

def getlinehash(arr):
    for quotient_str in arr:
        quotient = int(quotient_str)
        for divisor_str in arr:
            divisor=int(divisor_str)
            if quotient > divisor and quotient%divisor==0:
                return quotient/divisor

with open("input.txt",'rb') as f:
    hash = 0
    for line in f:
        words = line.split()
        hash += getlinehash(words)
print hash
            
