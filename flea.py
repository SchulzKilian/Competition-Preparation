x = input()

def isblack(x,y,S):
    if x%S == 0 or y%S == 0:
        return True
    fieldx = x//(S)
    fieldy = y//(S)
    if (fieldx + fieldy)%2 == 0:
        return True
    return False
    
while x != "0 0 0 0 0":
    pos = x.split()

    S,x,y,dx,dy= int(pos[0]), int(pos[1]), int(pos[2]), int(pos[3]), int(pos[4])


    maxtries = 10000
    step = 0
    while maxtries != 0:
        if not isblack(x,y,S):
            print(f"After {step} jumps the flea lands at ({x}, {y}).")
            break
        else:
            x += dx
            y += dy
            maxtries -=1
            step +=1
    if maxtries ==0:
        print("The flea cannot escape from black squares.")
            
    x = input()
            
        
        
        
