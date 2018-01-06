

class Layer():
    def __init__(self,id,range):
        self.id = id
        self.range = range
        if self.range:
            self.scanner_index = 0
            self.scanner_pointer=1
        else:
            self.scanner_index = None
    
    def print_layer(self):
        print "ID:", self.id,"\tRange:",self.range,"\tScanner Loc:",self.scanner_index
        
    def move_scanner(self):
        if self.scanner_index != None:
            "there is a scanner index"
            if (self.scanner_index+self.scanner_pointer) not in xrange(self.range):
                self.scanner_pointer*=-1
            self.scanner_index+=self.scanner_pointer
        
        
class Layers():
    def __init__(self):
        self.layer_arr=[]
        self.layer_id_arr=[]
        self.time = 0
        
    
    def add_layer(self,layer):
#       Adds sequential empty layers
        if len(self.layer_arr):
            while layer.id -1 > self.layer_id_arr[-1]:
                empty_layer = Layer(self.layer_id_arr[-1]+1,0)
                self.layer_arr.append(empty_layer)
                self.layer_id_arr.append(empty_layer.id)
#       Adds input layer
        self.layer_arr.append(layer)
        self.layer_id_arr.append(layer.id)
    
    def length(self):
        return len(self.layer_arr)
    
    def print_layers(self):
        for layer in self.layer_arr:
            layer.print_layer()
    
    def move_time(self):
        self.time+=1
        print "Time is now ", self.time, " picoseconds."
        for layer in self.layer_arr:
            layer.move_scanner()
    
    def scanner_caught(self):
        curr_layer = self.layer_arr[self.time]
        if curr_layer.scanner_index==0:
            severity = curr_layer.id * curr_layer.range
            print "The scanner caught you the severity is ", severity
            return severity
        return 0
#            layer.print_layer()
        
        
#    def add_layer(self,layer):





firewall = Layers()

with open("input1.txt",'rb') as f:
    for layer in f:
        arr=layer.replace(': ',',').strip().split(',')
        id = int(arr[0])
        range = int(arr[1])
        this_layer=Layer(id,range)
        firewall.add_layer(this_layer)

firewall.print_layers()
total_severity = 0

for x in xrange(firewall.length()-1):
    firewall.move_time()
    total_severity += firewall.scanner_caught()
firewall.print_layers()
print "The total severity of this route is ", total_severity
        