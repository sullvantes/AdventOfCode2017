    
#


def print_array(arr, digits):
#    max_len = max(len(arr[0]),len(arr[1]))
    for row_index in range(0,len(arr)):
        for item in arr[row_index]:
            item_length = len(str(item))
            print " "*(digits-item_length),
            print item,
        print "\n"

circ_mem =  [
                [142, 133, 122, 59],
                [5, 4, 2, 57],
                [10, 1, 1, 54],
                [11, 23, 25, 26]
            ]

large_loc = int(input("Please enter the highest location of your memory(exit with 999):"))
while large_loc!=999:
    next_loc=[0,-1]
    next_val = 0   
    edge_len = len(circ_mem)
    while next_val < large_loc:
    #top left corner
        y = next_loc[0]
        x = next_loc[1]
        if next_loc==[0,-1]: 
            for row in circ_mem:
                row.insert(0,0)    
            next_val = circ_mem[0][0] = circ_mem[0][1] + circ_mem[1][1]
            next_val = circ_mem[1][0]= circ_mem[0][0]+circ_mem[0][1] + circ_mem[1][1]+circ_mem[2][1] + circ_mem[2][0]
            next_loc=[2,0]
            edge_len+=1

    #left side
        elif x==0 and y>0 :
            if y<edge_len-1:
                next_val = circ_mem[y-1][x]+circ_mem[y-1][x+1] + circ_mem[y][x+1]
                if y < len(circ_mem)-1:
                    next_val += (circ_mem[y+1][x+1] + circ_mem[y+1][x])
                circ_mem[y][0]=next_val
                next_loc[0]+=1
    #bottom left corner
            elif y==edge_len-1:
                add_row=[0]*edge_len
                circ_mem.append(add_row)
                next_val = circ_mem[y][0]=circ_mem[y-1][x]+circ_mem[y-1][x+1] + circ_mem[y][x+1]
                next_loc[1]+=1

    #bottom
        elif y==edge_len-1:
            if x<edge_len:
                next_val = circ_mem[y][x-1]+circ_mem[y-1][x-1] + circ_mem[y-1][x]
                if x!=len(circ_mem[y])-1:
                    next_val+=circ_mem[y-1][x+1]
                circ_mem[y][x]= next_val
                next_loc[1]+=1
    #bottom right corner
            else:
                for row in circ_mem:
                    row.append(0)
                next_val = circ_mem[y][x]=circ_mem[y][x-1]+circ_mem[y-1][x-1]    
                next_loc[0]-=1
                edge_len+=1
    #right side    
        elif x==edge_len-1:
            if y>0:
                next_val = circ_mem[y][x]=circ_mem[y+1][x-1]+circ_mem[y][x-1]+circ_mem[y-1][x-1] + circ_mem[y+1][x]
                next_loc[0]-=1
            else:
                next_val = circ_mem[y][x]=circ_mem[y+1][x-1]+circ_mem[y][x-1] + circ_mem[y+1][x]
                add_row=[0]*edge_len
                circ_mem.insert(0,add_row)
                next_val = circ_mem[y][x]=circ_mem[y+1][x-1]+circ_mem[y][x-1] + circ_mem[y+1][x]
                next_loc[1]-=1
    #top
        elif y==0 and x>=0:
            next_val= circ_mem[y+1][x]+circ_mem[y+1][x+1] + circ_mem[y][x+1]
            if x!=0:
                next_val+=circ_mem[y+1][x-1]
                print circ_mem[y+1][x-1],
            circ_mem[y][x]=next_val
            print circ_mem[y+1][x], circ_mem[y+1][x+1], circ_mem[y][x+1]
            next_loc[1]-=1

        print_array(circ_mem, len(str(next_val)))
    large_loc = int(input("Please enter the highest location of your memory(exit with 999):"))
    
    

