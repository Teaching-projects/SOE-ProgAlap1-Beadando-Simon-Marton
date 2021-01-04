from typing import List, Set, Dict, Tuple, Optional
import json
import random

"""Ebben a moduleban foleg az alap mukodeshez szukseges logikai dolgok vannak benne, peldaul a jatek kezdeti terkepenek felallitasa, uj 2es berakasa, osszegzes, mozgatas stb..."""

def mapprint(map:list) -> None:
    """ A függveny ami kiirja a mapot """
    for i in range(4):
        print(map[i])


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


def win(map:list) -> bool:
    """A függvény ami megnézi hogy nyertünk-e"""
    for i in range(4):
        for j in range(4):
            if map[i][j] == 2048:
                return True
    
    return False

def lose(map:list) -> bool:
    """A függvény ami megnézi hogy vesztettünk-e"""
    nulla = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                nulla += 1
    if nulla == 0:
        return True
    else:
        return False
    

def get_current_state(map:list) -> str:
    """A fuggveny ami folyamatosan monitoralja a jatekos altal elert teljesitmenyt. """
    """Ha  valahol talalhato 2048, akkor nyert, ha nincs 2048, de talalhato 0, vagy a tobbi teljesul akkor nincsen vege a jateknak """
    """Ha pedig egyik sem teljesul akkor vesztettunk """
    if win(map) == True:
        return 'WON'          
    elif lose(map) == True:
        return 'LOST'
    else:
        return "GAME NOT OVER"
    
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

def összegez(map:list) -> list:
    """Az alabbi fuggveny osszegzi az egymas mellett levo ertekeket, majd visszaad egy valtozas erteket is ami alapbol false"""
    for i in range(len(map)):
        for j in range(len(map[i])- 1):
            if map[i][j] != 0 and map[i][j] == map[i][j + 1]:
                map[i][j] *= 2
                map[i][j + 1] = 0
    
    return map

def sorváltás(map:list) -> list:
    """A sorvaltas fuggveny akkor fontos, ha jobbra megyunk"""
    new_map = []
    for i in range(4):
        new_map.append([])
        for j in range(4):
            new_map[i].append(map[i][3-j])

    return new_map

def mapfordítás(map:list) -> list:
    """a mapfordítás function akkor fontos ha fel, vagy le megyunk"""
    new_map = []
    for i in range(4):
        new_map.append([])
        for j in range(4):
            new_map[i].append(map[j][i])
    
    return new_map

def mentés(map:list) -> None:
    """Az allas mentese"""
    import json
    file = open("állás.txt","w")
    json.dump(map, file)
    file.close()

def betöltés(filename:str) -> list:
    """Az elmentett allas betoltese, majd onnani folytatasa"""
    import json
    try:
        file = open(filename,"r")
        map = json.load(file)
        file.close()
    except:
        map = set_table()
    return map
    
def getcommand() -> str:
    """A command megadasa, majd visszakuldese"""
    command = input("Adj meg egy parancsot! ")
    return command

def move_left(map:list) -> list:
    """Balra mozgasnal eloszor osszehuzzuk az ertekeket, majd osszeadjuk oket, majd megint osszehuzzuk oket, majd ezt visszaadjuk"""
    new_map = összehúzás(map)
    new_map = összegez(new_map)
    new_map = összehúzás(new_map)
    return new_map

def move_right(map:list) -> list:
    """Jobbra mozgasnal sort fordítunk, balra mozgunk, visszafordítjuk a sort, majd visszaadjuk a megvaltozott terkepet"""
    new_map = sorváltás(map)
    new_map = move_left(new_map)
    new_map = sorváltás(new_map)
    return new_map

def move_up(map:list) -> list:
    """Ha fel akarunk mozogni, eloszor megfordítjuk a map sorait, es oszlopait, majd az ertekeket balra huzzuk, majd fordítunk megeggyet hogy az eredeti mapot visszakapjuk"""
    new_map = mapfordítás(map)
    new_map = move_left(new_map)
    new_map = mapfordítás(new_map)
    return new_map

def move_down(map:list) -> list:
    """Ha le akarunk mozogni, ugyanugy megfordítjuk a mapot, majd jobbra huzzuk az ertekeket, majd visszafordítjuk alapallasba"""
    new_map = mapfordítás(map)
    new_map = move_right(new_map)
    new_map = mapfordítás(new_map)
    return new_map


