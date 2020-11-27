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
    print("fel/le/balra/jobbra/end")
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

def összegez(map):
    újmap = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == map[i][]

    
###főprogram###

térkép = set_table()
térkép = give_new_2(map)
