import copy

class Program():
    def __init__(self,id):
        self.id = int(id)
        self.pipes=[]
        self.pipes_ids=[]
        self.zero=False
        
    def add_pipe(self,program):
        if program.id not in self.pipes_ids and program.id != self.id:
            self.pipes.append(program)
            self.pipes_ids.append(program.id)
    
    def print_prog(self):
        print "Program ID: ", self.id
        print "\tPipes:", self.pipes_ids  
        
    def shallow_find_zero(self):
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
        
    def deep_find_zero(self):
        if self.id == 0 or 0 in self.pipes_ids:
            self.zero = True 
#            print self.id, " gets to zero"
            for pipe in self.pipes:
                pipe.zero=True
#                print "/t", pipe.id, " gets to zero"
        else:
            for pipe in self.pipes:
                if pipe.find_zero():
                    self.zero = True
                    pipe.zero = True
                    return True
            self.zero=False
            return False

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

def make_zero_paths(programs,iteration):
    zero_progs = 0
    for program in programs.prog_arr:
        program.shallow_find_zero()

    for program in programs.prog_arr:
        if program.zero:
            zero_progs+=1
    print "Programs that reach 0 after ", iteration, " iteration:", zero_progs
    return zero_progs


all_progs = Programs()
with open("input.txt",'rb') as f:
    for program in f:
        #Making string of each program
        this_string=program.replace("<-> ",",").replace('\n','')
        this_arr = this_string.split(',')
#        print this_arr
        #add prog to all_progs if not present 
        if int(this_arr[0]) in all_progs.prog_id_arr:
            this_prog = all_progs.get_prog(int(this_arr[0]))
#            print "Existing prog", this_prog.id
        else:
            this_prog = Program(this_arr[0])
            all_progs.add_prog(this_prog)
#            print "New prog", this_prog.id
        #add pipes
        for index in range(1,len(this_arr)):
            pipe_id = int(this_arr[index])
            if all_progs.get_prog(pipe_id):
                pipe_prog = all_progs.get_prog(pipe_id)
#                print "\tNew Pipe", pipe_prog.id
            else:
                pipe_prog = Program(pipe_id)
                all_progs.add_prog(pipe_prog) 
#                print "\tNew Prog for Pipe", pipe_prog.id
            this_prog.add_pipe(pipe_prog)

zero_progs_last=1000000000
iteration = 1
zero_progs = make_zero_paths(all_progs,iteration)


while (zero_progs_last != zero_progs):
    iteration+=1
    zero_progs_last = zero_progs
    zero_progs = make_zero_paths(all_progs,iteration)
    

    
