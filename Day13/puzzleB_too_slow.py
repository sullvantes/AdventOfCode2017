

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
    
    def move_scanners(self):
        for layer in self.layer_arr:
            layer.move_scanner()
    
    def scanner_caught(self, packet_loc):
        curr_layer = self.layer_arr[packet_loc]
        if curr_layer.scanner_index==0:
            return True
        return 0
    
    def reset_scanners(self):
        for layer in self.layer_arr:
            if layer.scanner_index != None:
                layer.scanner_index = 0
                layer.scanner_pointer=1
    
    def escaped(self, packet_loc):
        if self.length() == packet_loc:
            return True
        return False


firewall = Layers()

with open("input.txt",'rb') as f:
    for layer in f:
        arr=layer.replace(': ',',').strip().split(',')
        id = int(arr[0])
        range = int(arr[1])
        this_layer=Layer(id,range)
        firewall.add_layer(this_layer)

through_safe=False
delay = 0

while(through_safe == False):
    time=0
    if delay>0:
        for x in xrange(0,delay):
            firewall.move_scanners()
            time+=1
    packet_loc=0
    while(not firewall.escaped(packet_loc) and not firewall.scanner_caught(packet_loc)):
        firewall.move_scanners()
        time+=1
        packet_loc+=1
        print "Delay:", delay, "Firewall length: ", firewall.length(), "Firewall Time:", time
    if firewall.escaped(packet_loc):
        through_safe=True
        print "Through safe == True"
    else:
        print "The Scanner caught you even with a", delay, "picosecond Delay."
        delay+=1
        firewall.reset_scanners()
print "the seconds Delay is ", delay