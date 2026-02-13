# Web VPython 3.2
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
    
    for i in range(L-1):
        for j in range(H-1):
            volt = values[i][j]

            dvx = float(values[i][j+1]) - float(values[i][j])
            dvy = float(values[i+1][j]) - float(values[i][j])
            
            Ex = -dvx
            Ey = -dvy
            
            E_norm = sqrt(Ex**2 + Ey**2)
            
            if E_norm > 0:
                Ex_normalized = (Ex / E_norm) * arrow_length
                Ey_normalized = (Ey / E_norm) * arrow_length
            else:
                Ex_normalized = 0
                Ey_normalized = 0
            
            arrow(pos = vector(j*4-(2*H), i*4-(2*L), 0), 
                  axis = vector(Ex_normalized, Ey_normalized, 0), 
                  color = color.orange)
                
    
f = read_local_file(scene.title_anchor)
floatages = csv_parse(f)
voltages = [[float(item) for item in sublist] for sublist in floatages]
grid(voltages)