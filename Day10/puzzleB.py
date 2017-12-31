
def knot(puzzle_list,location,instruction):
    sub_str = []
    for x in range(location,location+instruction):
        sub_str.append(puzzle_list[x%len(puzzle_list)])
    reversed_sub=list(reversed(sub_str))
    incr=0
    for x in range(location,location+instruction):
        puzzle_list[x%len(puzzle_list)] = reversed_sub[incr]
        incr+=1
instructions = []
#Get Instructions from File
with open("input.txt",'rb') as f:
    for line in f:
        for char in line:
            instructions.append(ord(char))
            
instructions.append(17) 
instructions.append(31)                     
instructions.append(73) 
instructions.append(47) 
instructions.append(23)

#print instructions


    

#Make list of consecutive numbers
list_length = 256 
puzzle_list = list(range(list_length))
#print puzzle_list

position = 0
skip_size = 0
#64 cycles
for cycle in range(0,64):
#    print cycle
    for instruction in instructions:
        if position > list_length:
            position = position%list_length
#        print "\tPosition: ", position    
#        print "\tInstruction:", instruction

        knot(puzzle_list,position,instruction)
#        print "\tNew Puzzle List: ", puzzle_list
#        print ''
        position+=(skip_size+instruction)
        skip_size+=1
#        
#        
dense_hash=''

for counter in range(0,255,16): 
    print counter
#    print puzzle_list
#    print puzzle_list[counter:counter+16]
    hash=puzzle_list[counter]
    for x in range(counter+1,counter+16):
        hash^=puzzle_list[x]
    print hex(hash)
    if len(hex(hash)[2:]) ==1:
        dense_hash+='0'
    dense_hash+=hex(hash)[2:]
print dense_hash
print '3efbe78a8d82f29979031a4aa0b16a9d'
print dense_hash == '3efbe78a8d82f29979031a4aa0b16a9d'
#
#
#    