import alapok
import scoring
import json
"""Meghívjuk az alapok modulet, ami segitsegevel osszerakom a foprogramot"""
"""Valamint a scoring module segitsegevel a jatekos folyamatosan kovetheti a scoret amit eddig elert"""

map = alapok.betöltés("állás.txt")
alapok.mapprint(map)

while(True):
    """legeloszor a command fuggvenyt meghivva bekerjuk a commandot, majd a kapot valaszt lekezeli az adott 6 if/elif statement"""

    """az ominozus command bekerese"""
    command = alapok.getcommand()

    if command == 'w':
        """ha a kommand a felfele mozgatas, eloszor elohivjuk a felfele mozgatas fuggvenyt az alapokbol, majd megvizsgaljuk a szelsosegeket, hogy nyertunk vagy vesztettunk e"""
        """Ha egyik sem igaz, akkor pedig elohivjuk a give_new_2 es a mapprint fuggvenyt, minden halad tovabb"""
        map = alapok.move_up(map)
        if alapok.win(map) == True:
            print("You have Won! Congratulations!")
            break
        elif alapok.lose(map) == True:
            print("You have Lost!")
            break
        elif alapok.vanenulla(map) == False and (alapok.vertical_move_exists(map) == True or alapok.horizontal_move_exists(map) == True):
            alapok.mapprint(map)
            print("erre nem tudsz már lépni de másik irányba igen")
            scoring.writescore(map, scoring.score(map))
        else:
            alapok.give_new_2(map)
            alapok.mapprint(map)
            scoring.writescore(map, scoring.score(map))
  
    # to move down 
    elif command  == 's':
        """A kovetkezo 3 fuggveny hasonlo modon mukodik mint az elozo: 1. megnezzuk mi a kommand, 2. szelsosegek vizsgalata, 3. ha nem nyertunk vagy vesztettunk akkor pedig folytatjuk"""
        map = alapok.move_down(map) 
        if alapok.win(map) == True:
            print("You have Won! Congratulations!")
            break
        elif alapok.lose(map) == True:
            print("You have Lost!")
            break
        elif alapok.vanenulla(map) == False and (alapok.vertical_move_exists(map) == True or alapok.horizontal_move_exists(map) == True):
            alapok.mapprint(map)
            print("erre nem tudsz már lépni de másik irányba igen")
            scoring.writescore(map, scoring.score(map))
        else:
            alapok.give_new_2(map)
            alapok.mapprint(map)
            scoring.writescore(map, scoring.score(map))
            
  
    # to move left 
    elif command == 'a': 
        """Ez is igy mukodik"""
        map = alapok.move_left(map)
        if alapok.win(map) == True:
            print("You have Won! Congratulations!")
            break
        elif alapok.lose(map) == True:
            print("You have Lost!")
            break
        elif alapok.vanenulla(map) == False and (alapok.vertical_move_exists(map) == True or alapok.horizontal_move_exists(map) == True):
            alapok.mapprint(map)
            print("erre nem tudsz már lépni de másik irányba igen")
            scoring.writescore(map, scoring.score(map))
        else:
            alapok.give_new_2(map)
            alapok.mapprint(map)
            scoring.writescore(map, scoring.score(map))

  
    # to move right 
    elif command == 'd':
        """Ez is igy mukodik"""
        map = alapok.move_right(map)
        if alapok.win(map) == True:
            print("You have Won! Congratulations!")
            break
        elif alapok.lose(map) == True:
            print("You have Lost!")
            break
        elif alapok.vanenulla(map) == False and (alapok.vertical_move_exists(map) == True or alapok.horizontal_move_exists(map) == True):
            alapok.mapprint(map)
            print("erre nem tudsz már lépni de másik irányba igen")
            scoring.writescore(map, scoring.score(map))
        else:
            alapok.give_new_2(map)
            alapok.mapprint(map)
            scoring.writescore(map, scoring.score(map))

    elif command == "save":
        """Ha a program megkapja a save kommandot, akkor egy egyfajta "Quicksave", lép érvénybe, az adott map eltárolásra kerül egy "Állás.txt", nevu fájlba, majd a program kilep"""
        score = scoring.score(map)
        alapok.mentés(map, score)
        break

    else:
        """Ha pedig nem azt az 5 lehetseges kommandot kaptuk amit az elso fuggveny leirt, akkor error uzenet, majd ujjabb command beadasa"""
        print("Rossz gomb")
    
