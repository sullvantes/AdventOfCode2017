from math import sqrt, ceil, floor

def find_middle_index(length):
    middle = float(length)/2
    if middle % 2 != 0:
        return int(middle)
    else:
        return int(middle + 1)
large_loc = int(input("Please enter the highest location of your memory(exit with 999):"))
while(large_loc != 999):    
#root of large_loc tells us how many layers there are
    root = int(floor(sqrt(large_loc)))
    
    if root**2 == large_loc:
        print "Steps are :", (root-1)
    else:
        corner = root**2+root+1 
#if the root is even the location would be on the bottom/left
        if root%2==0:
            print "Bottom/Left"
#if the root is odd the location would be on the bottom/left
        else:
            steps_to_edge = ceil(root/2.0)
            if large_loc==corner:
                print "Top/Right Corner"
            elif large_loc >=corner:
                print "Top"
                mid_side = corner + steps_to_edge
            else:
                print "Right"
                mid_side = root**2 + steps_to_edge
            steps = steps_to_edge + abs(large_loc - mid_side)
            print "Steps are :",int(steps)
    large_loc = int(input("Please enter the highest location of your memory(exit with 999:"))
    
    