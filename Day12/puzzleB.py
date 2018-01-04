import copy

class Program():
    def __init__(self,id):
        self.id = int(id)
        self.pipes=[]
        self.pipes_ids=[]
        self.zero=False
        self.group=None
        
    def add_pipe(self,program):
        if program.id not in self.pipes_ids and program.id != self.id:
            self.pipes.append(program)
            self.pipes_ids.append(program.id)
    
    def print_prog(self):
        print "Program ID: ", self.id
        print "\tPipes:", self.pipes_ids
        print "Group:", self.group
        
    def shallow_find_zero(self,group):
        zero_in_pipes = False
        for pipe in self.pipes:
            if pipe.zero:
                zero_in_pipes=True
        if self.id == 0 or zero_in_pipes:
            self.zero = True
#            print self.id, " gets to zero"
            for pipe in self.pipes:
                pipe.zero=True
#                print "\t", pipe.id, " gets to zero"
        
    def connect_group(self,group):
        this_group=None
        if self.group == group:
            this_group = group
        for pipe in self.pipes:
            if pipe.group==group:
                this_group=pipe.group
                break
        if this_group==group:
            self.group = this_group
#            print self.id, " gets to zero"
            for pipe in self.pipes:
                pipe.group=this_group
#                print "\t", pipe.id, " gets to zero"
        
    
class Programs():
    def __init__(self):
        self.prog_arr=[]
        self.prog_id_arr=[]
    
    def add_prog(self, program):
        if program.id not in self.prog_id_arr:
            self.prog_arr.append(program)
            self.prog_id_arr.append(int(program.id))
    
    def get_prog(self,id):
        for prog in self.prog_arr:
            if prog.id == id:
                return prog
        return False

    def undefined_groups(self):
        for prog in self.prog_arr:
            if prog.group == None:
                return True
        return False
    
    def create_new_group(self,group):
        if self.undefined_groups:
            for prog in self.prog_arr:
                if prog.group == None:
                    prog.group=group
                    break
            return True        
        return False
    
    

def make_zero_paths(programs,iteration):
    zero_progs = 0
    for program in programs.prog_arr:
        program.shallow_find_zero()

    for program in programs.prog_arr:
        if program.zero:
            zero_progs+=1
    print "Programs that reach 0 after ", iteration, " iteration:", zero_progs
    return zero_progs

def add_groups(programs,iteration, group):
    prog_count = 0
    for program in programs.prog_arr:
        program.connect_group(group)
    
    for program in programs.prog_arr:
        if program.group == group:
            prog_count+=1
    print "Programs that reach ", group," after ", iteration, " iteration:", prog_count
    return prog_count

def propagate_group(programs, group):
    iteration=1
    this_group_count_last = None
    this_group_count=add_groups(all_progs,iteration,this_group)

    #while number of group counts is changing, keep searching for more group members
    while (this_group_count_last != this_group_count):
        iteration+=1
        this_group_count_last = this_group_count
        this_group_count=add_groups(all_progs,iteration,this_group)





all_progs = Programs()
with open("input.txt",'rb') as f:
    for program in f:
        #Making string of each program
        this_string=program.replace("<-> ",",").replace('\n','')
        this_arr = this_string.split(',')
        #add prog to all_progs if not present 
        if int(this_arr[0]) in all_progs.prog_id_arr:
            this_prog = all_progs.get_prog(int(this_arr[0]))
        else:
            this_prog = Program(this_arr[0])
            all_progs.add_prog(this_prog)
        #add pipes
        for index in range(1,len(this_arr)):
            pipe_id = int(this_arr[index])
            if all_progs.get_prog(pipe_id):
                pipe_prog = all_progs.get_prog(pipe_id)
            else:
                pipe_prog = Program(pipe_id)
                all_progs.add_prog(pipe_prog) 
            this_prog.add_pipe(pipe_prog)
groups=0

#First group is zero
for program in all_progs.prog_arr:
    if program.id ==0:
        program.group=0
        this_group=0
        break
        
propagate_group(all_progs,this_group)

while all_progs.undefined_groups():
    this_group += 1
    all_progs.create_new_group(this_group)
    propagate_group(all_progs,this_group)
    

print this_group



        
#
#iteration=1
#this_group_count_last = None
#this_group_count=add_groups(all_progs,iteration,this_group)
#
##while number of group counts is changing, keep searching for more group members
#while (this_group_count_last != this_group_count):
#    iteration+=1
#    this_group_count_last = this_group_count
#    this_group_count=add_groups(all_progs,iteration,this_group)


    
