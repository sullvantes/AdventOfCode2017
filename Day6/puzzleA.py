    
def get_largest_index(arr):
    max_val = max(arr)
    for index, value in enumerate(arr):
        if value==max_val:
            return index, int(value)





mem_blocks=[]
with open("input.txt",'rb') as f:
    for line in f:
        mem_blocks= [int(x) for x in line.split()]

curr_mem=mem_blocks
mem_hist = []
new_mem = []
steps=0
while new_mem not in mem_hist:
    new_mem = curr_mem[:]
    mem_hist.append(curr_mem)
#    print "Memory History:", mem_hist
    index, value = get_largest_index(curr_mem)
    new_mem[index]=0
    index += 1
    while value>0:
        if index==len(new_mem):
            index=0
        new_mem[index] += 1
        index+=1
        value-=1
#    print "Current Configuration:", new_mem
    curr_mem = new_mem
    steps+=1
print steps

    
#for index, value in enumerate(curr_mem):
#    print index, value