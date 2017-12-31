
def knot(puzzle_list,location,instruction):
    sub_str = []
    for x in range(location,location+instruction):
        sub_str.append(puzzle_list[x%len(puzzle_list)])
    reversed_sub=list(reversed(sub_str))
    incr=0
    for x in range(location,location+instruction):
        puzzle_list[x%len(puzzle_list)] = reversed_sub[incr]
        incr+=1

#Get Instructions from File
with open("input.txt",'rb') as f:
    for line in f:
        instructions = map(int, line.split(","))
print instructions

#Make list of consecutive numbers
list_length = 256 
puzzle_list = list(range(list_length))
print puzzle_list

location = 0
skip_size = 0
for instruction in instructions:
    if location > list_length:
        location = location%list_length
    print "Location: ", location    
    print "Instruction:", instruction
    
    knot(puzzle_list,location,instruction)
    print "New Puzzle List: ", puzzle_list
    print ''
    location+=(skip_size+instruction)
    skip_size+=1
print "The First Two Multiplied is:", puzzle_list[0]*puzzle_list[1]



    