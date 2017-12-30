import operator

class Instruction():
    def __init__(self,instr):
        self.val=instr[0]
        self.operator=instr[1]
        self.change=eval(instr[2])
        self.eval_val=instr[3]
        self.eval_op=instr[4]
        self.eval_num=eval(instr[5])
        
    def eval_instr(self, lib):
        ops = {     
        "inc": operator.add, 
        "dec": operator.sub,
        "<" :  operator.lt,
        "<=" : operator.le,
        "==" : operator.eq,
        "!=" : operator.ne,
        ">=" : operator.ge,
        ">"  : operator.gt
        }
        
#        print "Evaluation", self.eval_val,ops[self.eval_op],self.eval_num
        print ops[self.eval_op](lib[self.eval_val],self.eval_num)
        return ops[self.eval_op](lib[self.eval_val],self.eval_num)
                
    def print_instr(self):
#        print "if", self.eval_val,self.eval_op,self.eval_num, "(",self.eval_instr(),")"
        print self.val,self.operator,self.change
        
            
        
        

jump_instr=[]
with open("input.txt",'rb') as f:
    for instr in f:
        this_instr = instr.replace('if','').split()
        print this_instr
        new_instr = Instruction(this_instr)
        jump_instr.append(new_instr)
        new_instr.print_instr()

ops = {     
        "inc": operator.add, 
        "dec": operator.sub,
        "<" :  operator.lt,
        "<=" : operator.le,
        "==" : operator.eq,
        "!=" : operator.ne,
        ">=" : operator.ge,
        ">"  : operator.gt
        }
                
value_dict = {}
count =1
highest_val=0
for instr in jump_instr:
    print count
    if instr.val not in value_dict:
        value_dict[instr.val]=0
        print "added",instr.val
    if instr.eval_val not in value_dict:
        value_dict[instr.eval_val]=0
        print "added",instr.eval_val
    if instr.eval_instr(value_dict):
        print "Following Instruction was executed"
#        print instr.eval_val, " = ", value_dict[instr.eval_val]
        new_val = ops[instr.operator](value_dict[instr.val],int(instr.change)) 
#        print new_val
        if new_val>highest_val:
            highest_val=new_val
        value_dict[instr.val] = new_val
#    instr.print_instr()
    count +=1
    print "\n",value_dict
#print ops["inc"](1,1) # prints 2 
#print ops["inc"](10,int('-10'))

for key, value in value_dict.items():
    try: highest_key
    except NameError: highest_key = key
    
    if value>=value_dict[highest_key]:
        highest_key=key
    
print highest_key , value_dict[highest_key]   

print highest_val
  # myVar exists.

