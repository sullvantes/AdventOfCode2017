import re

class Program():
    def __init__(self,arr):
        self.head = arr[0]
        self.weight = arr[1]
        self.children = []
        if len(arr) > 2:    
            for x in range(2,len(arr)):
                self.children.append(arr[x])
                
    def print_prog(self):
        if len(self.children)>0:
            mid=len(self.children)
            index = 1
            for child in self.children:
                if index == mid:
                    print self.head,"\t",child
                else:
                    print "\t",child
                index+=1
                if index == mid:
                    print self.head
                else:
                    print ""
                index+=1
                
        else:
            print self.head

def find_head(head,progs):
    for prog in progs:
        if head in prog.children:
            return find_head(prog.head,progs)
    return head    

prog_tree=[]
with open("input.txt",'rb') as f:
    for instr in f:
        this_prog_statement = instr.replace('-','')
        this_prog_statement = this_prog_statement.replace('>','')
        this_prog_statement = this_prog_statement.replace(',','')
        this_prog_statement = re.sub('\(','',this_prog_statement)
        this_prog_statement = re.sub('\)','',this_prog_statement)
        this_prog_arr = this_prog_statement.split()
        this_prog = Program(this_prog_arr)
        
        prog_tree.append(this_prog)

#for prog in prog_tree:
#    prog.print_prog()
    
start_head = prog_tree[0].head
print find_head(start_head,prog_tree)

#            sdfsdf
#            sdfsdf
#    dfdfsdf sdfsdf
#            sdfsdf
#            sdfsdf