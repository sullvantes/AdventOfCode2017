instr_list=[]
with open("input.txt",'rb') as f:
    for instr in f:
        instr_list.append(int(instr.strip()))
print instr_list                          

index=0
steps=0
while index<len(instr_list):
    instr = instr_list[index]
    steps += 1
    if instr_list[index] >=3:
        instr_list[index]-=1
    else:
        instr_list[index]+=1
    index += instr 
    
print steps