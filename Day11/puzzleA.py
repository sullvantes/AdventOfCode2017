
class Location():
    def __init__(self):
        #ne/sw
        self.x = 0
        #nw/se
        self.y = 0
        #n/s
        self.z = 0
        self.n = 0
        self.w = 0
    
    def step(self,step):
        if step == 'ne':
            self.x +=1
        elif step == 'sw':
            self.x -=1
        elif step == 'nw':
            self.y +=1
        elif step == 'se':
            self.y -=1
        elif step == 'n':
            self.z +=1
        elif step == 's':
            self.z -=1
        else:
            print "Invalid Step"
    
        
        if 'n' in step:
            self.n +=1
        elif 's' in step:
            self.n -=1
        if 'w' in step:
            self.w +=1
        elif 'e' in step:
            self.w -=1
        self.dist()
        
    def dist(self):
#        if self.x > 0:
#            print self.x, " steps Northeast"
#        elif self.x < 0:
#            print abs(self.x), " steps Southwest"
#        
#        if self.y > 0:
#            print self.y, " steps Northwest"
#        elif self.y < 0:
#            print abs(self.y), " steps Southeast"
#            
#        if self.z > 0:
#            print self.z, " steps North"
#        elif self.z < 0:
#            print abs(self.z), " steps South"
#            
#        if self.x==self.y==self.z==0:
#            print "End location is here."
        if abs(self.n)>abs(self.w):
            return (abs(self.n)+abs(self.w))
        else:
            return abs(self.w)
        
    def calc_dist(self):
        east = self.x - self.y
        print "EaSt :", east
        north = self.x+self.y+self.z
        print "north :", north
        
#        if self.x<0 and self.y<0:
#            return max(abs(self.x),abs(self.y))- self.z
#        elif self.x>0 and self.y>0:
#            return max(self.x,self.y) + self.z
#        else:
#            return "Not Calculated"
    
#    def print_coord(self):
#        print self.x , self.y, self.z
        
with open("input.txt",'rb') as f:
    for line in f:
        directions=line.split(",")
        
print directions
curr_loc = Location()
max_loc = curr_loc.dist()
for direction in directions:
    curr_loc.step(direction)
#    print "Steps Away :" , curr_loc.dist()
    max_loc = max(curr_loc.dist(),max_loc)
   

print max_loc

    