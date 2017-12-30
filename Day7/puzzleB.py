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
    
    def prog_weight(self,prog_list):
        prog_weight = int(self.weight)
        for child in self.children:
            for prog in prog_list:
                if prog.head == child:
                    prog_weight += int(prog.prog_weight(prog_list))
        return prog_weight
    
    def isBalanced(self,prog_list):
        if len(self.children)>0:
            weights = []
            for child in self.children:
                for prog in prog_list:
                    if child ==prog.head:
                        weights.append(prog.prog_weight(prog_list))
            if not weights[1:] == weights[:-1]:
                print self.head
                print self.weight
                print self.children
                print weights

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
    

#start_head = prog_tree[0].head
#print find_head(start_head,prog_tree)

for prog in prog_tree:
    prog.prog_weight(prog_tree)
    
for prog in prog_tree:
    prog.isBalanced(prog_tree)
    
for prog in prog_tree:
    if prog.head == 'vmttcwe':
        print prog.head, prog.weight
    
    
    




#            sdfsdf
#            sdfsdf
#    dfdfsdf sdfsdf
#            sdfsdf
#            sdfsdf