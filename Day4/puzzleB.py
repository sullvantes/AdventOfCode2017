#import csv
#
def order_name(inp):
    return ''.join(sorted(inp))

def is_Valid(passphrase):
    checked = []
    mutated_pass=[]
    for name in passphrase:
        mutated_pass.append(order_name(name))
    for name in mutated_pass:
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