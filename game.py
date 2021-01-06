import json
import alapok
import scoring
from typing import List, Set, Dict, Tuple, Optional


def start():
    """This will generate the map, or saves in the map from allas.txt if it exists.

    Returns:
        None: This justs prints the table
    """
    map = alapok.betoltes("állás.txt")
    alapok.mapprint(map)
    return map
print(start.__doc__)

def up(map:list) -> list:
    """The function to move up and handle the state t´where the player is at right now

    Args:
        map (list): The map u want to change and handle

    Returns:
        list: the changed version of the map
    """
    map = alapok.move_up(map)
    if alapok.win(map) == True:
        print("You have Won! Congratulations!")

    elif alapok.lose(map) == True:
        print("You have Lost!")

    elif alapok.vanenulla(map) == False and (alapok.vertical_move_exists(map) == True or alapok.horizontal_move_exists(map) == True):
        alapok.mapprint(map)
        print("erre nem tudsz már lépni de másik irányba igen")
        scoring.writescore(map, scoring.score(map))

    else:
        alapok.give_new_2(map)
        alapok.mapprint(map)
        scoring.writescore(map, scoring.score(map))

    return map
print(up.__doc__)

def down(map:list) -> list:
    """The function that moves down the map and gets the state of the game

    Args:
        map (list): the map u want to investigate

    Returns:
        list: The changed map
    """
    map = alapok.move_down(map)
    if alapok.win(map) == True:
        print("You have Won! Congratulations!")

    elif alapok.lose(map) == True:
        print("You have Lost!")

    elif alapok.vanenulla(map) == False and (alapok.vertical_move_exists(map) == True or alapok.horizontal_move_exists(map) == True):
        alapok.mapprint(map)
        print("erre nem tudsz már lépni de másik irányba igen")
        scoring.writescore(map, scoring.score(map))
    else:
        alapok.give_new_2(map)
        alapok.mapprint(map)
        scoring.writescore(map, scoring.score(map))

    return map
print(down.__doc__)

def left(map:list) -> list:
    """The map that handles the move down command, and gets the state of the game

    Args:
        map (list): The map u want to change

    Returns:
        list: ´The changed map
    """
    map = alapok.move_left(map)
    if alapok.win(map) == True:
        print("You have Won! Congratulations!")

    elif alapok.lose(map) == True:
        print("You have Lost!")

    elif alapok.vanenulla(map) == False and (alapok.vertical_move_exists(map) == True or alapok.horizontal_move_exists(map) == True):
        alapok.mapprint(map)
        print("erre nem tudsz már lépni de másik irányba igen")
        scoring.writescore(map, scoring.score(map))
    else:
        alapok.give_new_2(map)
        alapok.mapprint(map)
        scoring.writescore(map, scoring.score(map))
    return map
print(left.__doc__)

def right(map:list) -> list:
    """The function that handles the move right command and gets the state of the game

    Args:
        map (list): The map u want to change

    Returns:
        list: The changed state of the game
    """
    map = alapok.move_right(map)
    if alapok.win(map) == True:
        print("You have Won! Congratulations!")

    elif alapok.lose(map) == True:
        print("You have Lost!")

    elif alapok.vanenulla(map) == False and (alapok.vertical_move_exists(map) == True or alapok.horizontal_move_exists(map) == True):
        alapok.mapprint(map)
        print("erre nem tudsz már lépni de másik irányba igen")
        scoring.writescore(map, scoring.score(map))
    else:
        alapok.give_new_2(map)
        alapok.mapprint(map)
        scoring.writescore(map, scoring.score(map))
    return map
print(right.__doc__)

def save(score:int,map:list) -> None:
    """The function that saves the score and map

    Args:
        score (int): The score u want to save
        map (list): The map u want to save
    """
    score = scoring.score(map)
    alapok.mentes(map, score)
print(save.__doc__)

def badcommand() -> str:
    """If you entered a bad command and error message will pop up

    Returns:
        str: An error mesage
    """
    print("Rossz gomb")
print(badcommand.__doc__)

def basics(command:str,map:list) -> list:
    """This will handle every single command and what happens after that

    Args:
        command (str): The command
        map (list): The map u want to change

    Returns:
        list: The changed map
    """
    if command == "w":
        map = up(map)
    elif command == "s":
        map = down(map)
    elif command == "a":
        map = left(map)
    elif command == "d":
        map = right(map)
    elif command == "save":
        score = scoring.score(map)
        save(score,map)
    else:
        badcommand()
    return map
print(basics.__doc__)

def main() -> None:
    """Generates the map, and also handles the basic function
    """
    map = start()

    while(True):
        command = alapok.getcommand()
        map = basics(command,map)
print(main.__doc__)