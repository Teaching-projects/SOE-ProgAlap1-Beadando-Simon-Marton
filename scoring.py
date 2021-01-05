from typing import List, Set, Dict, Tuple, Optional
"""A module, ami a scoringot csinälja, a scoring egyszeru, amennyi szam van a tablan, a score egyenlo annak a 10X-sevel"""
"""Valamint plusban az 1024 +500, a 2048 +1000 pontot jelent"""

def score(map:list) -> int:
    """Allscore változo bevezetesevel 3 for ciklussal elintezem a pontok kiszamitasat"""

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
    """Ebben pedig kiiratom oket"""
    allscore = score(map)
    print("Your current score is: {}".format(allscore))