import alapok
import json
"""Meghívjuk az alapok modulet, ami segitsegevel osszerakom a foprogramot"""

map = alapok.betöltés("állás.txt")
alapok.mapprint(map)

while(True):
    """legeloszor a command fuggvenyt meghivva bekerjuk a commandot, majd a kapot valaszt lekezeli az adott 6 if/elif statement"""

    """az ominozus command bekerese"""
    command = alapok.getcommand()

    if command == 'w':
        """Ha a kommand az hogy menjen minden fel, akkor elohivjuk a move_up fuggvenyt, majd lekerjuk a statuszt. a statusz megadja hol tart a jatekos, az alapjan 3 lehetseges vegkimenetel van."""
        """Ha azt kapjuk vissza hogy "Game not over", akkor elohivjuk a give_new_2 fuggvenyt es minden megy tovább"""
        """Ha pedig azt kapjuk hogy "Game over", vagy "Won", akkor pedig vege van a jateknak, egy breakkel pedig kilepunk a programbol"""
        map = alapok.move_up(map)
        if alapok.win(map) == True:
            print("You have Won! Congratulations!")
            break
        elif alapok.lose(map) == True:
            print("You have Lost!, Try Again!")
            break
        else:
            alapok.give_new_2(map)
            alapok.mapprint(map)
  
    # to move down 
    elif command  == 's':
        """A kovetkezo 3 fuggveny hasonlo modon mukodik mint az elozo: 1. megnezzuk mi a kommand, 2. lekerjuk a statuszt, 3. a statusz alapjan levonjuk a kovetkeztetest"""
        map = alapok.move_down(map) 
        if alapok.win(map) == True:
            print("You have Won! Congratulations!")
            break
        elif alapok.lose(map) == True:
            print("You have Lost!, Try Again!")
            break
        else:
            alapok.give_new_2(map)
            alapok.mapprint(map)
            
  
    # to move left 
    elif command == 'a': 
        """Ez is igy mukodik"""
        map = alapok.move_left(map)
        if alapok.win(map) == True:
            print("You have Won! Congratulations!")
            break
        elif alapok.lose(map) == True:
            print("You have Lost!, Try Again!")
            break
        else:
            alapok.give_new_2(map)
            alapok.mapprint(map)

  
    # to move right 
    elif command == 'd':
        """Ez is igy mukodik"""
        map = alapok.move_right(map)
        if alapok.win(map) == True:
            print("You have Won! Congratulations!")
            break
        elif alapok.lose(map) == True:
            print("You have Lost!, Try Again!")
            break
        else:
            alapok.give_new_2(map)
            alapok.mapprint(map)

    elif command == "save":
        """Ha a program megkapja a save kommandot, akkor egy egyfajta "Quicksave", lép érvénybe, az adott map eltárolásra kerül egy "Állás.txt", nevu fájlba, majd a program kilep"""
        alapok.mentés(map)
        break

    else:
        """Ha pedig nem azt az 5 lehetseges kommandot kaptuk amit az elso fuggveny leirt, akkor error uzenet, majd ujjabb command beadasa"""
        print("Rossz gomb")
    
