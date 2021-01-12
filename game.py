import json
import alapok
import sys
from typing import List, Set, Dict, Tuple, Optional
listexample1 = [[2,2,2,2],[2,2,2,2],[0,0,0,0],[0,0,0,0]]
listexample2 = [[2,2,2,2],[16,16,16,16],[4,4,4,4],[2,0,2,2]]
listexample3 = [[8,8,8,8],[8,8,8,8],[0,0,0,0],[2,2,2,2048]]
def give_instructions() -> None:
    """Gives out the instructions to the player
    """
    print("Üdvözöllek a 2048-as játékban, a aprancsok a következők: ")
    print("w-fel/a-balra/s-le/d-jobbra/store-kimentés,befejezés")
    print("a játék kimenti ahol állsz ha az end parancsot nyomod meg, sok szerencsét")
    print("Add meg a parncsot")

def writescore(map:list) -> None:
    """This will print out the score

    Args:
        map (list): The map used to calculate the score
    """
    print("Your current score is: {}".format(alapok.score(map)))

def start() -> None:
    """This will load a new map, or loads in the map from allas.txt if it exists.

    Returns:
        None: This justs prints the table
    """
    give_instructions()
    map = load("allas.txt")
    alapok.mapprint(map)
    writescore(map)
    return map

def get_current_state(map:list) -> None:
    """This function will check what happens to the map after a command has been given out. Did the player lose, did the player win, etc...

    Args:
        map (list): [description]
    """
    if alapok.win(map) == True:
        print("You have Won! Congratulations!")
        sys.exit()
    elif alapok.lose(map) == True:
        print("You have Lost!")
        sys.exit()
    elif alapok.is_there_zero(map) == False and (alapok.vertical_move_exists(map) == True or alapok.horizontal_move_exists(map) == True):
        alapok.mapprint(map)
        print("erre nem tudsz már lépni de másik irányba igen")
        writescore(map)
    else:
        alapok.give_new_2(map)
        alapok.mapprint(map)
        writescore(map)

def save(map:list, score:int) -> None:
    """This will save the map and the score u are currently at
    """
    import json
    file = open("allas.txt","w")
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
        map = alapok.set_table()
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

def bad_command() -> str:
    """If you entered a bad command and error message will pop up

    Returns:
        str: An error message
    """
    print("Rossz gomb")



def basics(command:str,map:list) -> list:
    """This will handle every single command and what happens after that

    Args:
        command (str): The command
        map (list): The map u want to change

    Returns:
        list: The changed map
    """
    if command == "w":
        map = alapok.move_up(map)
        get_current_state(map)
    elif command == "s":
        map = alapok.move_down(map)
        get_current_state(map)
    elif command == "a":
        map = alapok.move_left(map)
        get_current_state(map)
    elif command == "d":
        map = alapok.move_right(map)
        get_current_state(map)
    elif command == "save":
        score = alapok.score(map)
        save(map,score)
    else:
        bad_command()
    return map

def main() -> None:
    """Generates the map, and also handles the basic function
    """
    map = start()
    

    while(True):
        command = alapok.getcommand()
        map = basics(command,map)