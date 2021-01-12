from typing import List, Set, Dict, Tuple, Optional
import json
import random
listexample1 = [[2,2,2,2],[2,2,2,2],[0,0,0,0],[0,0,0,0]]
listexample2 = [[2,2,2,2],[16,16,16,16],[4,4,4,4],[2,0,2,2]]
listexample3 = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]]

def mapprint(map:list) -> None:
    """The function that prints out the map

    Args:
        map (list): The map that is given here will be printed out

    >>> mapprint(listexample1)
    [2, 2, 2, 2]
    [2, 2, 2, 2]
    [0, 0, 0, 0]
    [0, 0, 0, 0]
    >>> mapprint(listexapmle2)
    [2, 2, 2, 2]
    [16, 16, 16, 16]
    [4, 4, 4, 4]
    [2, 2, 2, 2]
    >>> mapprint(listexample3)
    [8, 8, 8, 8]
    [8, 8, 8, 8]
    [0, 0, 0, 0]
    [2, 2, 2, 2048]
    """
    for i in range(4):
        print(map[i])


def give_new_2(map:list) -> None:
    """A function that will put a new 2 in a random location where 0-s are present

    Args:
        map (list): The map that u want to use
    >>> give_new_2(listexample1)
    [[2, 2, 2, 2], [2, 2, 2, 2], [0, 0, 0, 0], [2, 0, 0, 0]]
    >>> give_new_2(listexample2)
    [[2, 2, 2, 2], [16, 16, 16, 16], [4, 4, 4, 4], [2, 2, 2, 2]]
    """
    sor = random.randint(0,3)
    oszlop = random.randint(0,3)
    while map[sor][oszlop] != 0:
        sor = random.randint(0,3)
        oszlop = random.randint(0,3)
    map[sor][oszlop] = 2

def set_table() -> None:
    """This is the start of everything, this will generate the first table, with a 2 in a random  place

    Returns:
        None: This returns nothing, only prints out the table
    
    >>> set_table()
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]]
    """
    map = []
    for i in range(4):
        sor = [0]*4
        map.append(sor)

    give_new_2(map)

    return map

def win(map:list) -> bool:
    """The function that will check if you have won yet or not

    Args:
        map (list): It will check in this map

    Returns:
        bool: Will give a true if you have won and a false if you haven't won'
    >>> win(listexample1)
    False
    >>> win(listexample2)
    False
    >>> win(listexample3)
    True
    """
    for i in range(4):
        for j in range(4):
            if map[i][j] == 2048:
                return True
    
    return False


def can_it_merge_horizontally(map:list) -> bool:
    """This is used in the lose function and checks if you can merge horizontally or not

    Args:
        map (list): it checks in this map

    Returns:
        bool: Return a True if you can, a false if you can't
    
    >>> can_it_merge_horizontally(listexample1)
    True
    >>> can_it_merge_horizontally(listexample2)
    True
    >>> can_it_merge_horizontally(listexample3)
    True
    """
    for i in range(len(map)):
        for j in range(len(map[i])-1):
            if map[i][j] == map[i][j + 1]:
                return True
    
    return False


def can_it_merge_vertically(map:list) -> bool:
    """This function checks whether you can merge vertically or not

    Args:
        map (list): The list u want to check

    Returns:
        bool: Rteurn a true if you can a false otherwise
    >>> can_it_merge_vertically(listexample1)
    True
    >>> can_it_merge_vertically(listexample2)
    False
    >>> can_it_merge_vertically(listexample3)
    True
    """
    for i in range(len(map)-1):
        for j in range(len(map[i])):
            if map[i][j] == map[i + 1][j]:
                return True
    
    return False

def is_there_zero(map:list) -> bool:
    """This function checks if there is a 0 on the map

    Args:
        map (list): The map u are checking in

    Returns:
        bool: True if there is a 0 on the map and false otherwise
    >>> is_there_zero(listexample1)
    True
    >>> is_there_zero(listexample2)
    True
    >>> is_there_zero(listexample3)
    True
    """
    nulla = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                return True
    return False

def lose(map:list) -> bool:
    """This function checks if you have lost or not. If there isnt any 0-s and you cant move vertically or horizontally, you have lost

    Args:
        map (list): The map u are checking in

    Returns:
        bool: Return a True if you Lost, a false if you didnt'
    
    >>> lose(listexample1)
    False
    >>> lose(listexample2)
    False
    >>> lose(listexample3)
    False
    """
    if not is_there_zero(map) and not can_it_merge_vertically(map) and not can_it_merge_horizontally(map):
        return True
    else:
        return False



def pull_together(map:list) -> list:
    """This function will reutrn a new map, that is basically the same, but has no zeros inbetween the numbers

    Args:
        map (list): The map u are using

    Returns:
        list: The pulled form of the map
    
    >>> pull_together(listexample1)
    [[2, 2, 2, 2], [2, 2, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> pull_together(listexample2)
    [[2, 2, 2, 2], [16, 16, 16, 16], [4, 4, 4, 4], [2, 2, 2, 0]]
    >>> pull_together(listexample3)
    [[8, 8, 8, 8], [8, 8, 8, 8], [0, 0, 0, 0], [2, 2, 2, 2048]]
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


def merge(map:list) -> list:
    """It will add the numbers together always in left direction, and will use other functions to get other directions done

    Args:
        map (list): The map u are checking in

    Returns:
        list: The added map
    >>> merge(listexample1)
    [[4, 0, 4, 0], [4, 0, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> merge(listexample2)
    [[4, 0, 4, 0], [32, 0, 32, 0], [8, 0, 8, 0], [2, 0, 4, 0]]
    >>> merge(listexample3)
    [[16, 0, 16, 0], [16, 0, 16, 0], [0, 0, 0, 0], [4, 0, 2, 2048]]
    """
    for i in range(len(map)):
        for j in range(len(map[i])- 1):
            if map[i][j] != 0 and map[i][j] == map[i][j + 1]:
                map[i][j] *= 2
                map[i][j + 1] = 0
    
    return map


def reverse(map:list) -> list:
    """
    This will reverse the map

    Args:
        map (list): The map u are reversing

    Returns:
        list: The reversed version of map
    >>> reverse(listexample1)
    [[2, 2, 2, 2], [2, 2, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> reverse(listexample2)
    [[2, 2, 2, 2], [16, 16, 16, 16], [4, 4, 4, 4], [2, 2, 0, 2]]
    >>> reverse(listexample3)
    [[8, 8, 8, 8], [8, 8, 8, 8], [0, 0, 0, 0], [2048, 2, 2, 2]] 
    """
    new_map = []
    for i in range(4):
        new_map.append([])
        for j in range(4):
            new_map[i].append(map[i][3-j])

    return new_map

def transpose(map:list) -> list:
    """This will interchange the maps coluumns and rows

    Args:
        map (list): The map u are interchaning

    Returns:
        list: The interchanged version of the map
    >>> transpose(listexample1)
    [[2, 2, 0, 0], [2, 2, 0, 0], [2, 2, 0, 0], [2, 2, 0, 0]]
    >>> transpose(listexample2)
    [[2, 16, 4, 2], [2, 16, 4, 0], [2, 16, 4, 2], [2, 16, 4, 2]]
    >>> transpose(listexample3)
    [[8, 8, 0, 2], [8, 8, 0, 2], [8, 8, 0, 2], [8, 8, 0, 2048]]
    """
    new_map = []
    for i in range(4):
        new_map.append([])
        for j in range(4):
            new_map[i].append(map[j][i])
    
    return new_map

def save(map:list, score:int) -> None:
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

def load(filename:str) -> list:
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

def getcommand() -> str:
    """The function to get the command

    Returns:
        str: The command
    >>> getcommand()
    s
    """
    command = input("Adj meg egy parancsot! ")
    return command

def score(map:list) -> int:
    """The function that calculates the score that the player has. First it calculates every number that is on the table, than the value gets multiplied by 10

    Args:
        map (list): The map

    Returns:
        int: The claculated score
    """
    allscore = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            tempscore = map[i][j] * 10
            allscore += tempscore
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1024:
                allscore += 500
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 2048:
                allscore += 1000
                
    return allscore

def move_left(map:list) -> list:
    """The function to handle the left moving command. First u pull the map together, than add the numbers, then pull again

    Args:
        map (list): the map u want to change

    Returns:
        list: the changed map

    >>> move_left(listexample1)
    [[4, 4, 0, 0], [4, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> move_left(listexample2)
    [[4, 4, 0, 0], [32, 32, 0, 0], [8, 8, 0, 0], [4, 2, 0, 0]]
    >>> move_left(listexample3)
    [[16, 16, 0, 0], [16, 16, 0, 0], [0, 0, 0, 0], [4, 2, 2048, 0]]
    """
    new_map = pull_together(map)
    new_map = merge(new_map)
    new_map = pull_together(new_map)
    return new_map


def move_right(map:list) -> list:
    """The function to handle when u want to move right. First u reverse the map, then u use the move left function, that u reverse again to get the default map

    Args:
        map (list): The map u want to change

    Returns:
        list: The changed version of the map

    >>> move_right(listexample1)
    [[0, 0, 4, 4], [0, 0, 4, 4], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> move_right(listexample2)
    [[0, 0, 4, 4], [0, 0, 32, 32], [0, 0, 8, 8], [0, 0, 2, 4]]
    >>> move_right(listexample3)
    [[0, 0, 16, 16], [0, 0, 16, 16], [0, 0, 0, 0], [0, 2, 4, 2048]]
    """
    new_map = reverse(map)
    new_map = move_left(new_map)
    new_map = reverse(new_map)
    return new_map


def move_up(map:list) -> list:
    """The function that handles the up command. First u interchang the map, than u move left, than u interchange again to get the default map

    Args:
        map (list): The map u want to change

    Returns:
        list: The changed map

    >>> move_up(listexample1)
    [[4, 4, 4, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> move_up(listexample2)
    [[2, 2, 2, 2], [16, 16, 16, 16], [4, 4, 4, 4], [2, 0, 2, 2]]
    >>> move_up(listexample3)
    [[16, 16, 16, 16], [2, 2, 2, 2048], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    new_map = transpose(map)
    new_map = move_left(new_map)
    new_map = transpose(new_map)
    return new_map

def move_down(map:list) -> list:
    """The function that handles the move down command, nfirst u interchange the map, than u move right, than u interchange again to get the default map

    Args:
        map (list): the map u want to change

    Returns:
        list: The changed map
    >>> move_down(listexample1)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 4, 4, 4]]
    >>> move_down(listexample2)
    [[2, 0, 2, 2], [16, 2, 16, 16], [4, 16, 4, 4], [2, 4, 2, 2]]
    >>> move_down(listexample3)
    [[0, 0, 0, 0], [0, 0, 0, 0], [16, 16, 16, 16], [2, 2, 2, 2048]]
    """
    new_map = transpose(map)
    new_map = move_right(new_map)
    new_map = transpose(new_map)
    return new_map

