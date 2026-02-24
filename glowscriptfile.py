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
    H = len(values[0])
    arrow_length = 3
    
    #Finding max_E
    max_E = 0
    for i in range(L-1):
        for j in range(H-1):
            # volt = values[i][j]

            dvx = values[i][j+1] - values[i][j]
            dvy = values[i+1][j] - values[i][j]
            
            Ex = -dvx
            Ey = -dvy
            
            E_norm = sqrt(Ex**2 + Ey**2)
            if E_norm > max_E: 
                max_E = E_norm
        
        if max_E == 0: 
            max_E = 1 #to not divide by 0
        
    for i in range(L-1): 
        for j in range(H-1): 
            dvx = values[i][j+1] - values[i][j]
            dvy = values[i+1][j] - values[i][j] 
            
            Ex = -dvx 
            Ey = -dvy 
            
            E_norm = sqrt(Ex**2 + Ey**2) 
            
            if E_norm > 0:
                Ex_normalized = (Ex / E_norm) * arrow_length
                Ey_normalized = (Ey / E_norm) * arrow_length
            else:
                Ex_normalized = 0
                Ey_normalized = 0
            
             # fixed to log, but still has the weird outlier 0.0V part !
             # left this code so i wouldn't mess up the consistency/integrity of the code for the rest - eileen
            opav = 0.2 + 0.8 * (log(1 + E_norm) / log(1 + max_E))
            
            arrow(pos = vector(j*4-(2*H), i*4-(2*L), 0), 
                  axis = vector(Ex_normalized, Ey_normalized, 0), 
                  color = color.cyan, 
                  opacity = opav)
           
    
f = read_local_file(scene.title_anchor)
floatages = csv_parse(f)
voltages = [[float(item) for item in sublist] for sublist in floatages]
grid(voltages)