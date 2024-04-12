import random
from config import GAME_CHOIES, RULSE, scoreboard


from datetime import datetime

def get_system_choies():
    """
    This function performs a random selection from GAME_CHOIES
    """
    system_choies = random.choice(GAME_CHOIES)
    return system_choies

def get_user_choies():
    """
    This function takes input from the user and checks that there is no mistake
    """
    user_input = input("Enter your choies (r, p, s): ")
    if user_input not in GAME_CHOIES:
        print("oops!!, something went wrong, Try again... ")
        return get_user_choies()
    return user_input

def find_winner(usre, system):
    """
    who is the winner??
    """
    match = {usre , system}

    if len(match) == 1:
        return None

    return RULSE[tuple(sorted(match))]

def update_scoreboard(result):
    """
    this is a score board is user want to play again...
    """
    if result['user'] == 3:
        scoreboard['user'] += 1
    if result['system'] == 3:
        scoreboard['system'] += 1
    
    print('#' * 22)
    print("##" ,f'user: {scoreboard["user"]}'.ljust(16) , "##")
    print('##' ,f'system: {scoreboard["system"]}'.ljust(16) , '##')
    print('#' * 22)

def do_you_want_play_again():
    response = input("do you want play again? (y/n): ")

    if response == 'y':
        play()
    elif response == 'n':
        print("good game :)")
    else:
        print("yes or no!! (y/n): ")
        do_you_want_play_again()

def play():
    result = {'user':0 , 'system':0}

    while result['user'] < 3 and result['system'] < 3:
        user_choies = get_user_choies()
        system = get_system_choies()
        winner = find_winner(user_choies, system )
        

        if winner == user_choies:
            result['user'] += 1
            msg = "You Win" 
        elif winner == system:
            result['system'] += 1
            msg = "You Lose"
        else:
             msg = "Drow"

        print(f"Your choise:{user_choies}, system: {system}, winner:{msg} ")

    update_scoreboard(result)
    play_again= do_you_want_play_again()
    


if __name__ == '__main__':
    start_play = datetime.now()
    play()
    end_play = datetime.now()
    durasion = end_play - start_play
    print(
        f"total play: {durasion.seconds // 3600}: {durasion.seconds // 60}:" 
        f"{durasion.seconds % 60} "
         )
    