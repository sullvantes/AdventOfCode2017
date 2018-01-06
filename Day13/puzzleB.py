with open("input.txt",'rb') as f:
    layers = [map(int, l.strip().split(': ')) for l in f]
    firewall_size = layers[-1][0]+1
    delay = 0
    while True:
        for layer in layers:
            n = layer[1]-1
            v = (delay + layer[0])% (n*2) 
            v = 2 * n - v if v>=n else v
            if v==0:
                break
        else:
            break
        delay += 1
    print delay
    
    
#### AFTER LOOKING AT Reddit and using the algorithm to know where the scanner is 