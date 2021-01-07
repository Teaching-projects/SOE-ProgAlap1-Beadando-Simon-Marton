from typing import List, Set, Dict, Tuple, Optional

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

def writescore(map:list, allscore:int) -> None:
    """This will print out the score

    Args:
        map (list): The map used to calculate the score
        allscore (int): The score itself
    """
    allscore = score(map)
    print("Your current score is: {}".format(allscore))