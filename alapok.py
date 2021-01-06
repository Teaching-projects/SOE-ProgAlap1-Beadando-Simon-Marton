from typing import List, Set, Dict, Tuple, Optional
import json
import random

def mapprint(map:list) -> None:
    """The function that prints out the map

    Args:
        map (list): The map that is given here will be printed out
    """
    for i in range(4):
        print(map[i])
print(mapprint.__doc__)

#test

#lista = [[2,2,2,2],[2,2,2,2],[0,0,0,0],[0,0,0,0]]
#lista2 = [[2,2,2,2],[16,16,16,16],[4,4,4,4],[2,2,2,2]]
#lista3 = [[2,2,2,2],[2,2,2,2],[0,0,0,0],[0,0,0,0]]
#lista4 = [[0,0,0,0],[2,2,2,2],[2,2,2,2],[0,0,0,0]]
#lista5 = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]]
#print(mapprint(lista))
#print(mapprint(lista2))
#print(mapprint(lista3))
#print(mapprint(lista4))
#print(mapprint(lista5))


def give_new_2(map:list) -> None:
    """A function that will put a new 2 in a random location where 0-s are present

    Args:
        map (list): The map that u want to use
    """
    sor = random.randint(0,3)
    oszlop = random.randint(0,3)
    if map[sor][oszlop] == 0:
        map[sor][oszlop] = 2
    else:
        while map[sor][oszlop] != 0:
            sor = random.randint(0,3)
            oszlop = random.randint(0,3)
        map[sor][oszlop] = 2
print(give_new_2.__doc__)
#test
#lista = [[2,2,2,2],[2,2,2,2],[0,0,0,0],[0,0,0,0]]
#lista2 = [[0,0,0,0],[2,2,2,2],[2,2,2,2],[0,0,0,0]]
#lista3 = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]]
#give_new_2(lista)
#give_new_2(lista2)
#give_new_2(lista3)
#print(lista)
#print(lista2)
#print(lista3)


def set_table():
    """This is the start of everything, this will generate the first table, with a 2 in a random  place

    Returns:
        None: This returns nothing, only prints out the table
    """
    map = []
    for i in range(4):
        sor = [0]*4
        map.append(sor)

    print("Üdvözöllek a 2048-as játékban, a aprancsok a következők: ")
    print("w-fel/a-balra/s-le/d-jobbra/save-kimentés,befejezés")
    print("a játék kimenti ahol állsz ha az end parancsot nyomod meg, sok szerencsét")
    print("Add meg a parncsot")
    give_new_2(map)

    return map
print(set_table.__doc__)
#test
#print(set_table())

def win(map:list) -> bool:
    """The function that will check if you have won yet or not

    Args:
        map (list): It will check in this map

    Returns:
        bool: Will give a true if you have won and a false if you haven't won'
    """
    for i in range(4):
        for j in range(4):
            if map[i][j] == 2048:
                return True
    
    return False
print(win.__doc__)
#test

#lista = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]] -> True
#lista2 = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,0]] -> False
#print(win(lista))
#print(win(lista2))


def horizontal_move_exists(map:list) -> bool:
    """This is used in the lose function and checks if you can move horizontally

    Args:
        map (list): it checks in this map

    Returns:
        bool: Return a True if you can, a false if you can't
    """
    for i in range(len(map)):
        for j in range(len(map[i])-1):
            if map[i][j] == map[i][j + 1]:
                return True
    
    return False
print(horizontal_move_exists.__doc__)
#test
#lista = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]]
#print(horizontal_move_exists(lista))


def vertical_move_exists(map:list) -> bool:
    """This will check if you can move vertically or not, also used in the lose function

    Args:
        map (list): The map u checking in

    Returns:
        bool: Return a True if you can, a false if you can't
    """
    for i in range(len(map)-1):
        for j in range(len(map[i])):
            if map[i][j] == map[i + 1][j]:
                return True
    
    return False
print(vertical_move_exists.__doc__)
#test
#lista = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]]
#print(vertical_move_exists(lista))


def lose(map:list) -> bool:
    """This function checks if you have lost or not. If there isnt any 0-s and you cant move vertically or horizontally, you have lost

    Args:
        map (list): The map u are checking in

    Returns:
        bool: Return a True if you Lost, a false if you didnt'
    """
    nulla = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                nulla += 1
    if nulla == 0 and (vertical_move_exists(map) == False and horizontal_move_exists(map) == False):
        return True
    else:
        return False
print(lose.__doc__)
#test
#lista = [[2,4,256,2],[4,8,16,64],[16,32,512,1024],[256,16,4,64]]
#lista1 = [[8,8,8,8],[8,8,8,8],[8,4,8,4],[2,16,2,2]]
#lista2 = [[8,8,8,8],[8,8,8,8],[32,64,32,64],[2,8,2,16]]
#lista3 = [[8,8,8,8],[8,8,8,8],[1024,2,4,16],[2,16,2,16]]
#lista4 = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,16,2,16]]
#print(mapprint(lista))
#print(lose(lista))
#print(lose(lista1))
#print(lose(lista2))
#print(lose(lista3))
#print(lose(lista4))

def vanenulla(map:list) -> bool:
    """This function checks if there is a 0 on the map

    Args:
        map (list): The map u are checking in

    Returns:
        bool: True if there is a 0 on the map and false otherwise
    """
    nulla = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                return True
    return False
print(vanenulla.__doc__)

def osszehuzas(map:list) -> list:
    """This function will pull the numbers in the map together

    Args:
        map (list): The map u are using

    Returns:
        list: The pulled form of the map
    """
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
print(osszehuzas.__doc__)
#test
#lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
#lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
#print(osszehuzas(lista))
#print(osszehuzas(lista2))


def osszegez(map:list) -> list:
    """It will add the numbers together, and puts a ^on the second part

    Args:
        map (list): The map u are checking in

    Returns:
        list: The added map
    """
    for i in range(len(map)):
        for j in range(len(map[i])- 1):
            if map[i][j] != 0 and map[i][j] == map[i][j + 1]:
                map[i][j] *= 2
                map[i][j + 1] = 0
    
    return map
print(osszegez.__doc__)
#test
#lista = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
#print(osszegez(lista)), az output:
#[[2, 0, 4, 0], [4, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0]]


def sorvaltas(map:list) -> list:
    """
    This will reverse the map

    Args:
        map (list): The map u are reversing

    Returns:
        list: The reversed version of map
    """
    new_map = []
    for i in range(4):
        new_map.append([])
        for j in range(4):
            new_map[i].append(map[i][3-j])

    return new_map
print(sorvaltas.__doc__)
#test
#lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
#lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
#print(sorvaltas(lista))
#print(sorvaltas(lista2))

def mapforditas(map:list) -> list:
    """This will interchange the maps coluumns and rows

    Args:
        map (list): The map u are interchaning

    Returns:
        list: The interchanged version of the map
    """
    new_map = []
    for i in range(4):
        new_map.append([])
        for j in range(4):
            new_map[i].append(map[j][i])
    
    return new_map
print(mapforditas.__doc__)
#test
#lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
#lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
#print(mapforditas(lista))
#print(mapforditas(lista2))

def mentes(map:list, score:int) -> None:
    """This will save the map and the score u are currently at
    """
    import json
    file = open("állás.txt","w")
    data = {
        "map": map,
        "score": score,
    }
    json.dump(data, file)
    file.close()
print(mentes.__doc__)

def betoltes(filename:str) -> list:
    """This will load the data that you have saved

    Returns:
        list: the saved list
    """
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
print(betoltes.__doc__)

def getcommand() -> str:
    """The function to get the command

    Returns:
        str: The command
    """
    command = input("Adj meg egy parancsot! ")
    return command
print(getcommand.__doc__)
#Test
#print(getcommand())

def move_left(map:list) -> list:
    """The function to handle the left moving command. First u pull the map together, than add the numbers, then pull again

    Args:
        map (list): the map u want to change

    Returns:
        list: the changed map
    """
    new_map = osszehuzas(map)
    new_map = osszegez(new_map)
    new_map = osszehuzas(new_map)
    return new_map
print(move_left.__doc__)
#test
#lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
#lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
#print(move_left(lista))
#print(move_left(lista2))


def move_right(map:list) -> list:
    """The function to handle when u want to move right. First u reverse the map, then u use the move left function, that u reverse again to get the default map

    Args:
        map (list): The map u want to change

    Returns:
        list: The changed version of the map
    """
    new_map = sorvaltas(map)
    new_map = move_left(new_map)
    new_map = sorvaltas(new_map)
    return new_map
print(move_right.__doc__)
#test
#lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
#lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
#print(move_right(lista))
#print(move_right(lista2))


def move_up(map:list) -> list:
    """The function that handles the up command. First u interchang the map, than u move left, than u interchange again to get the default map

    Args:
        map (list): The map u want to change

    Returns:
        list: The changed map
    """
    new_map = mapforditas(map)
    new_map = move_left(new_map)
    new_map = mapforditas(new_map)
    return new_map
print(move_up.__doc__)
#test
#lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
#lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
#print(move_up(lista))
#print(move_up(lista2))

def move_down(map:list) -> list:
    """The function that handles the move down command, nfirst u interchange the map, than u move right, than u interchange again to get the default map

    Args:
        map (list): the map u want to change

    Returns:
        list: The changed map
    """
    new_map = mapforditas(map)
    new_map = move_right(new_map)
    new_map = mapforditas(new_map)
    return new_map
print(move_down.__doc__)
#test
#lista = [[8,8,0,8],[8,8,0,8],[0,0,0,0],[2,2,2,0]]
#lista2 = [[2,0,2,2],[2,2,0,2],[0,0,0,0],[0,0,0,0]]
#print(move_down(lista))
#print(move_down(lista2))

