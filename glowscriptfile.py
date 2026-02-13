Web VPython 3.2

def csv_parse(fd): # specify file
    items = []
    text = fd.text
    for line in iter(text.splitlines()):
        if len(line.strip()) > 1 :
            items.append(line.strip().split(','))
    return items
            
        
def grid(values):
    L = len(values)
    H = len(values[1])
    for i in range(L):
        for j in range(H):
            volt = values[i][j]
            dvx = values[i+1][j] - values[i][j]
            dvy = values[i][j+1] - values[i][j]
            arrow(pos = vector(j*4-(2*H), i*4-(2*L), 0), axis=vec(3,1,0), color=color.orange)
            
            # x positions increase to the right, but y positions 
            # increase going upwards
                
    
f = read_local_file(scene.title_anchor)
floatages = csv_parse(f)
voltages = [[float(item) for item in sublist] for sublist in floatages]



grid(voltages)

 