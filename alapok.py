from typing import List, Set, Dict, Tuple, Optional
import json
import random

"""Ebben a moduleban foleg az alap mukodeshez szukseges logikai dolgok vannak benne, peldaul a jatek kezdeti terkepenek felallitasa, uj 2es berakasa, osszegzes, mozgatas stb..."""

def mapprint(map:list) -> None:
    """ A függveny ami kiirja a mapot """
    for i in range(4):
        print(map[i])

"""Teszteles"""
"""
lista = [[2,2,2,2],[2,2,2,2],[0,0,0,0],[0,0,0,0]]
lista2 = [[2,2,2,2],[16,16,16,16],[4,4,4,4],[2,2,2,2]]
lista3 = [[2,2,2,2],[2,2,2,2],[0,0,0,0],[0,0,0,0]]
lista4 = [[0,0,0,0],[2,2,2,2],[2,2,2,2],[0,0,0,0]]
lista5 = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]]
print(mapprint(lista))
print(mapprint(lista2))
print(mapprint(lista3))
print(mapprint(lista4))
print(mapprint(lista5))
"""

def give_new_2(map:list) -> None:
    """Ez a fuggveny mindig belerak egy terkepbe egy 2est, de csak oda ahol 0-as van"""
    sor = random.randint(0,3)
    oszlop = random.randint(0,3)
    if map[sor][oszlop] == 0:
        map[sor][oszlop] = 2
    else:
        while map[sor][oszlop] != 0:
            sor = random.randint(0,3)
            oszlop = random.randint(0,3)
        map[sor][oszlop] = 2
"""Teszteles"""
"""
lista = [[2,2,2,2],[2,2,2,2],[0,0,0,0],[0,0,0,0]]
lista2 = [[0,0,0,0],[2,2,2,2],[2,2,2,2],[0,0,0,0]]
lista3 = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]]
give_new_2(lista)
give_new_2(lista2)
give_new_2(lista3)
print(lista)
print(lista2)
print(lista3)
"""

def set_table():
    """A fuggveny ami a jatek elejen inicializalja a mapot, mjad egyezeteti a jatekossal a lehetseges parancsokat"""
    map = []
    for i in range(4):
        sor = [0]*4
        map.append(sor)

    """A lehetseges parancsok listaja"""

    print("Üdvözöllek a 2048-as játékban, a aprancsok a következők: ")
    print("w-fel/a-balra/s-le/d-jobbra/save-kimentés,befejezés")
    print("a játék kimenti ahol állsz ha az end parancsot nyomod meg, sok szerencsét")
    print("Add meg a parncsot")
    give_new_2(map)

    return map

"""teszteles"""
"""print(set_table())"""




def win(map:list) -> bool:
    """A függvény ami megnézi hogy nyertünk-e"""
    for i in range(4):
        for j in range(4):
            if map[i][j] == 2048:
                return True
    
    return False
"""Teszteles"""
"""
lista = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]] -> True
lista2 = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,0]] -> False
print(win(lista))
print(win(lista2))
"""

def horizontal_move_exists(map:list) -> bool:
    for i in range(len(map)):
        for j in range(len(map[i])-1):
            if map[i][j] == map[i][j + 1]:
                return True
    
    return False
"""Teszteles"""
"""
lista = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]]
print(horizontal_move_exists(lista))
"""

def vertical_move_exists(map:list) -> bool:
    for i in range(len(map)-1):
        for j in range(len(map[i])):
            if map[i][j] == map[i + 1][j]:
                return True
    
    return False
"""Teszteles"""
"""
lista = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]]
print(vertical_move_exists(lista))
"""

def lose(map:list) -> bool:
    """A függvény ami megnézi hogy vesztettünk-e"""
    nulla = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                nulla += 1
    if nulla == 0 and (vertical_move_exists(map) == False and horizontal_move_exists(map) == False):
        return True
    else:
        return False
"""Teszteles"""
"""
lista = [[2,4,256,2],[4,8,16,64],[16,32,512,1024],[256,16,4,64]]
lista1 = [[8,8,8,8],[8,8,8,8],[8,4,8,4],[2,16,2,2]]
lista2 = [[8,8,8,8],[8,8,8,8],[32,64,32,64],[2,8,2,16]]
lista3 = [[8,8,8,8],[8,8,8,8],[1024,2,4,16],[2,16,2,16]]
lista4 = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,16,2,16]]
print(mapprint(lista))
print(lose(lista))
print(lose(lista1))
print(lose(lista2))
print(lose(lista3))
print(lose(lista4))
"""

def vanenulla(map):
    nulla = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                return True
    return False
def összehúzás(map:list) -> list:
    """Az alabbi fuggveny kulcsfontossagu, ugyanis ez osszehuzza terkepen talalhato elemeket, majd returnuli egy uj_map nevu valtozoban, es egy valtozas nevu booleannal, ami megvizsgalja tortent-e valtozas"""
    new_map = []

    for i in range(4):
        new_map.append([0] * 4)

    for i in range(4): 
        pos = 0
        for j in range(4): 
            if (map[i][j] != 0): 
                new_map[i][pos] = map[i][j] 
                pos += 1
    return new_map
"""Teszteles"""
"""
lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
print(összehúzás(lista))
print(összehúzás(lista2))
"""

def összegez(map:list) -> list:
    """Az alabbi fuggveny osszegzi az egymas mellett levo ertekeket, majd visszaad egy valtozas erteket is ami alapbol false"""
    for i in range(len(map)):
        for j in range(len(map[i])- 1):
            if map[i][j] != 0 and map[i][j] == map[i][j + 1]:
                map[i][j] *= 2
                map[i][j + 1] = 0
    
    return map
"""Teszteles"""
"""
lista = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
print(összegez(lista)), az output:
[[2, 0, 4, 0], [4, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0]]
"""


def sorváltás(map:list) -> list:
    """A sorvaltas fuggveny akkor fontos, ha jobbra megyunk"""
    new_map = []
    for i in range(4):
        new_map.append([])
        for j in range(4):
            new_map[i].append(map[i][3-j])

    return new_map
"""Teszteles"""
"""
lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
print(sorváltás(lista))
print(sorváltás(lista2))
"""
def mapfordítás(map:list) -> list:
    """a mapfordítás function akkor fontos ha fel, vagy le megyunk"""
    new_map = []
    for i in range(4):
        new_map.append([])
        for j in range(4):
            new_map[i].append(map[j][i])
    
    return new_map
"""Teszteles"""
"""
lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
print(mapfordítás(lista))
print(mapfordítás(lista2))
"""
def mentés(map:list, score:int) -> None:
    """Az allas mentese"""
    import json
    file = open("állás.txt","w")
    data = {
        "map": map,
        "score": score,
    }
    json.dump(data, file)
    file.close()

def betöltés(filename:str) -> list:
    """Az elmentett allas betoltese, majd onnani folytatasa"""
    import json
    try:
        file = open(filename,"r")
        data = json.load(file)
        global map
        global score
        map = data["map"]
        score = data["score"]
        file.close()
    except:
        map = set_table()
        score = 0
    return map

def getcommand() -> str:
    """A command megadasa, majd visszakuldese"""
    command = input("Adj meg egy parancsot! ")
    return command
"""Teszteles"""

def move_left(map:list) -> list:
    """Balra mozgasnal eloszor osszehuzzuk az ertekeket, majd osszeadjuk oket, majd megint osszehuzzuk oket, majd ezt visszaadjuk"""
    new_map = összehúzás(map)
    new_map = összegez(new_map)
    new_map = összehúzás(new_map)
    return new_map
"""Teszteles"""
"""
lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
print(move_left(lista))
print(move_left(lista2))
"""

def move_right(map:list) -> list:
    """Jobbra mozgasnal sort fordítunk, balra mozgunk, visszafordítjuk a sort, majd visszaadjuk a megvaltozott terkepet"""
    new_map = sorváltás(map)
    new_map = move_left(new_map)
    new_map = sorváltás(new_map)
    return new_map
"""Teszteles"""
"""
lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
print(move_right(lista))
print(move_right(lista2))
"""

def move_up(map:list) -> list:
    """Ha fel akarunk mozogni, eloszor megfordítjuk a map sorait, es oszlopait, majd az ertekeket balra huzzuk, majd fordítunk megeggyet hogy az eredeti mapot visszakapjuk"""
    new_map = mapfordítás(map)
    new_map = move_left(new_map)
    new_map = mapfordítás(new_map)
    return new_map
"""Teszteles"""
"""
lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
print(move_up(lista))
print(move_up(lista2))
"""

def move_down(map:list) -> list:
    """Ha le akarunk mozogni, ugyanugy megfordítjuk a mapot, majd jobbra huzzuk az ertekeket, majd visszafordítjuk alapallasba"""
    new_map = mapfordítás(map)
    new_map = move_right(new_map)
    new_map = mapfordítás(new_map)
    return new_map
"""Teszteles"""
"""
lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
print(move_down(lista))
print(move_down(lista2))
"""

