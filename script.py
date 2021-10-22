import random, colorama, os
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
clear = lambda: os.system('clear') # clears terminal

print("Welcome to Dosjack. A terminal based game about the gambling game black jack.")
print("==========")
print("Controls:\n-p [play]      -help [displays help]\n-se [settings] -h [hit]\n-s [stand]\n-co [controls]")
print("==========")

startinput = input("")

# reads value/deck of whomever
def read_integers(filename):
    infoFile = open(filename, 'r')
    score_num = [] # the int value of whats in the file
    for number in infoFile:
        score_num.append(int(number))
    return score_num

""" ### might not need these lines of codes
# adds the values up
def add_integers_to_deck(number_value):
    add =sum(number_value)
"""

# chooses random number for dealer & player
def randomnumber():
    return random.randrange(1, 21)

def gamestart():
    ### Saving and writing into txt file for dealer and player
    d_save_path = open('dealercards.txt', 'w+') # creates/saves & clears whatever was in file priorer 
    p_save_path = open('playercards.txt', 'w+') # creates/saves & clears whatever was in file priorer

    d_save_path.write(str((randomnumber())))
    p_save_path.write(str((randomnumber())))

    d_save_path.close() # closes writing/file
    p_save_path.close() # closes writing/file

    clear()

    ### Reads & Prints
    d_readfile = open('dealercards.txt', 'r')
    if d_readfile.mode == 'r':
        contents = d_readfile.read()
        print("Dealer Cards:")
        print(str(contents))
    
    p_readfile = open('playercards.txt', 'r')
    if p_readfile.mode == 'r':
        contents = p_readfile.read()
        print("Your cards: ")  
        print(str(contents))

def player_hit():
    clear()
    
    p_save_path = open('playercards.txt', 'a+') # adds onto file via appending
    p_save_path.write("\n") # creates new line
    p_save_path.write(str((randomnumber())))
    p_save_path.close()

    p_readfile = open('dealercards.txt', 'r')
    dealercards = read_integers('dealercards.txt')
    playercards = read_integers('playercards.txt')

    if p_readfile.mode == 'r':
        contents = p_readfile.read()
        print("Dealer Cards:")
        print(sum(dealercards))

    print("Your cards:")
    print(sum(playercards)) # adds new int to cards)

def dealer_hit():
    clear()
    
    d_save_path = open('dealercards.txt', 'a+') # adds onto file via appending
    d_save_path.write("\n") # creates new line
    d_save_path.write(str((randomnumber())))
    d_save_path.close()

    d_readfile = open('dealercards.txt', 'r')
    dealercards = read_integers('dealercards.txt')
    playercards = read_integers('playercards.txt')

    if d_readfile.mode == 'r':
        contents = d_readfile.read()
        print("Dealer Cards:")
        print(sum(dealercards))

    print("Your cards:")
    print(sum(playercards)) # adds new int to cards)

main_menu1 = 1
controls_menu = 0
help_menu = 0
settings_menu = 0

playing_game = 0
listiner_game = 0
replay_game = 0

while main_menu1 == 1:
    if startinput == str("-co"): # controls
        main_menu1 = 0 # turns off main menu while loop
        controls_menu = 1 # turns on controls menu while loop
        while controls_menu == 1:
            clear()
            print("==========")
            print("Controls:\n-p [play]      -help [displays help]\n-s [settings]  -h [hit]\n-d [double]    -co [controls]")
            print("==========\n-esc to leave menu")
            controlsmenu_userinput = input("input: ")
            if controlsmenu_userinput == str("-esc"):
                clear()
                print("Welcome to Dosjack. A terminal based game about the gambling game black jack.")
                print("==========")
                print("Controls:\n-p [play]      -help [displays help]\n-se [settings] -h [hit]\n-s [stand]\n-co [controls]")

                print("==========")
                controls_menu = 0
                main_menu1 = 1
                startinput = input("") # resets startinput
    if startinput == str("-help"): # help
        main_menu1 = 0
        help_menu = 1
        while help_menu == 1:
            clear()
            print("==========")
            print("How to play:\nIn DOSjack, all you have to do is get blackjack (score: 21) or have a higher score than the dealer.\nIf you're score is over 21 or under the dealer's score. You lose. This logic applies to the dealer too. When a game is finished, just press enter a few times to reset it.")
            print("==========")
            print("Controls:\n-p [play]      -help [displays help]\n-se [settings] -h [hit]\n-s [stand]\n-co [controls]")
            print("==========\n-esc to leave menu")
            help_userinput = input("input: ")
            if help_userinput == str("-esc"):
                clear()
                print("Welcome to Dosjack. A terminal based game about the gambling game black jack.")
                print("==========")
                print("Controls:\n-p [play]      -help [displays help]\n-se [settings] -h [hit]\n-s [stand]\n-co [controls]")
                print("==========")
                help_menu = 0
                main_menu1 = 1
                startinput = input("") # resets startinput
    if startinput == str("-se"):
        main_menu1 = 0
        settings_menu = 1
        while settings_menu == 1:
            clear()
            print(f"{Fore.LIGHTRED_EX}Feature has not been implemented yet")
            print("==========\n-esc to leave menu")
            settings_userinput = input("input: ")
            if settings_userinput == str("-esc"):
                clear()
                print("Welcome to Dosjack. A terminal based game about the gambling game black jack.")
                print("==========")
                print("Controls:\n-p [play]      -help [displays help]\n-se [settings] -h [hit]\n-s [stand]\n-co [controls]")
                print("==========")
                settings_menu = 0
                main_menu1 = 1
                startinput = input("") # resets startinput
        
    if startinput == str("-p"): # play
        main_menu1 = 0
        playing_game = 1
      
while playing_game == 1:
    gamestart()
    userinput = input()

    if userinput == str("-h"): # if the player is hitting as their first choice
        player_hit()
        playing_game = 0
        listiner_game = 1
        while listiner_game == 1: # creates a infinite listening loop
            playercards = read_integers('playercards.txt')
            dealercards = read_integers('dealercards.txt')

            if sum(playercards) == 21: # if player scores blackjack
                print(f"{Fore.LIGHTGREEN_EX}Blackjack!")
            if sum(playercards) > 21: # if player scores blackjack
                print(f"{Fore.LIGHTRED_EX}Dealer wins")

            userinput = input("") # resets the userinput
            if userinput == str("-h"):
                player_hit()
            if userinput == str("-s"):
                dealer_hit()
                if sum(dealercards) == 21: # if dealer scores black jack
                    print(f"{Fore.LIGHTRED_EX}Dealer wins")
                if sum(playercards) < sum(dealercards) and sum(dealercards) < 21: # if dealer scores higher than player
                    print(f"{Fore.LIGHTRED_EX}Dealer wins")
                if sum(playercards) > sum(dealercards) and sum(dealercards) < 21: # if player scores higher than dealer
                    print(f"{Fore.LIGHTGREEN_EX}Player wins")
                if sum(playercards) < sum(dealercards) and sum(dealercards) > 21: # if player scores higher than dealer
                    print(f"{Fore.LIGHTGREEN_EX}Player wins")
            if userinput == str(""):
                listiner_game = 0
                playing_game = 1
                userinput = input("")

    if userinput == str("-s"): # for when the player wants to sit as their first choice
        dealer_hit()
        listiner_game = 1
        while listiner_game == 1: # creates a infinite listening loop
            playercards = read_integers('playercards.txt')
            dealercards = read_integers('dealercards.txt')

            if sum(dealercards) == 21: # if dealer scores black jack
                print(f"{Fore.LIGHTRED_EX}Dealer wins")
            if sum(playercards) < sum(dealercards) and sum(dealercards) < 21: # if dealer scores higher than player
                print(f"{Fore.LIGHTRED_EX}Dealer wins")
            if sum(playercards) > sum(dealercards) and sum(dealercards) < 21: # if player scores higher than dealer
                print(f"{Fore.LIGHTGREEN_EX}Player wins")
            if sum(playercards) < sum(dealercards) and sum(dealercards) > 21: # if player scores higher than dealer
                print(f"{Fore.LIGHTGREEN_EX}Player wins")
            userinput = input("") # resets the userinput
            if userinput == str("-s"):
                dealer_hit()
            if userinput == str("-h"):
                player_hit()
            if userinput == str(""):
                listiner_game = 0
                playing_game = 1
                userinput = input("")