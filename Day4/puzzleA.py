import csv

def is_Valid(passphrase):
    checked = []
    for name in passphrase:
        if name in checked:
            return False
        else:
            checked.append(name)
    return True
            





passphrases = []
count =0
with open("input.txt",'rb') as f:
    for passphrase in f:
        names=passphrase.split()
        if is_Valid(names):
            count +=1
        else:
            print names

print count

