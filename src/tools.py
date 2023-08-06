import os, curses, re

def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear') 

def computemove(map, direction, cords):
    currentx = cords[0]
    currenty = cords[1]

    startposstatus = map[currenty][currentx]

    if startposstatus == 1:
        raise "INVAILID START POS"
    
    if direction == 'w':
        newy = currenty - 1
        newx = currentx
    
    elif direction == 's':
        newy = currenty + 1
        newx = currentx
    
    elif direction == 'a':
        newy = currenty
        newx = currentx - 1
    
    elif direction == 'd':
        newy = currenty
        newx = currentx + 1

    else:
        newy = currenty
        newx = currentx
    
    if map[newy][newx] == 1:
        return [currentx, currenty]
    else:
        return [newx, newy]
