#2048
import random
import json

def mapprint(map):
    for i in range(4):
        print(map[i])

def set_table():
    map = []
    for i in range(4):
        sor = [0]*4
        map.append(sor)

    print("Üdvözöllek a 2048-as játékban, a aprancsok a következők: ")
    print("w-fel/a-balra/s-le/d-jobbra/end-kimentés,befejezés")
    print("a játék kimenti ahol állsz ha az end parancsot nyomod meg, sok szerencsét")
    
    return map

def give_new_2(map):
    sor = random.randint(0,3)
    oszlop = random.randint(0,3)
    if map[sor][oszlop] != 0:
        sor = random.randint(0,3)
        oszlop = random.randint(0,3)
    map[sor][oszlop] = 2
    
    mapprint(map)

def win(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 2048:
                return True
            else:
                return False

def lose(map):
    nullák = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                nullák.append(map[i][j])
    if len(nullák) == 0:
        return True
    else:
        return False

def összehúzás(mat): 
   
    változás = False
    new_map = [] 

    for i in range(4): 
        new_mat.append([0] * 4) 

    for i in range(4): 
        pos = 0
  
        for j in range(4): 
            if(mat[i][j] != 0): 
                
                new_mat[i][pos] = mat[i][j] 
                  
                if(j != pos): 
                    changed = True
                pos += 1
    return new_map, változás

def összegez(map):
    változás = False
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (map[i][j] == 0 and map[i][j + 1] == 0) and map[i][j] != 0:
                map[i][j] = map[i][j] *2
                map[i][j+1] = 0
                változott = True
    
    return map, változás

def sorváltás(map):
    new_map = []
    for i in range(len(4)):
        new_map.append([])
        for j in range(len(4)):
            new_map[i].append(map[i][3-j])

    return new_map

def mapfordítás(map):
    new_map = []
    for i in range(4):
        new_map.append([])
        for j in range(4):
            new_map[i].append(map[j][i])
    
    return new_map

def mentés(map):
    import json
    file = open("állás.txt","wt")
    json.dump(map, file)
    file.close()

def betöltés(map):
    import json
    file = open("állás.txt","rt")
    map = json.load(file)
    file.close()
    return map

def getdirection():
    direction = input("Adj meg egy irányt! ")
    return direction

###főprogram###
térkép = set_table()
while True:
    tékép = give_new_2(map)
    direction = getdirection()
    if direction == "a":

    
