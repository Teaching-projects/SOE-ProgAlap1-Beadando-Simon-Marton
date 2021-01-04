import alapok
import json

mentesek_szama = 0
if mentesek_szama == 0:
    map = alapok.set_table()
if mentesek_szama > 0:
    map = alapok.betöltés(map)

while(True):
  
    command = alapok.getcommand()
    if command == 'w': 
        map = alapok.move_up(map)
        status = alapok.get_current_state(map) 
        if(status == 'GAME NOT OVER'): 
            alapok.give_new_2(map)   
        elif status == 'GAME OVER':
            print("Game Over")
            break
        elif status == 'WON':
            print("You have won")
            break
  
    # to move down 
    elif command  == 's': 
        map = alapok.move_down(map) 
        status = alapok.get_current_state(map) 
        if(status == 'GAME NOT OVER'): 
            alapok.give_new_2(map) 
        elif status == 'GAME OVER':
            print("Game Over")
            break
        elif status == 'WON':
            print("You have won")
            break
            
  
    # to move left 
    elif command == 'a': 
        map = alapok.move_left(map) 
        status = alapok.get_current_state(map) 
        if status == 'GAME NOT OVER': 
            alapok.give_new_2(map) 
        elif status == 'GAME OVER':
            print("Game Over")
            break
        elif status == 'WON':
            print("You have won")
            break
  
    # to move right 
    elif command == 'd':
        map = alapok.move_right(map)
        status = alapok.get_current_state(map)  
        if(status == 'GAME NOT OVER'): 
            alapok.give_new_2(map) 
        elif status == 'GAME OVER':
            print("Game Over")
            break
        elif status == 'WON':
            print("You have won")
            break
    elif command == "save":
        mentesek_szama += 1
        alapok.mentés(map)
        break
    else: 
        print("Rossz gomb")
    
