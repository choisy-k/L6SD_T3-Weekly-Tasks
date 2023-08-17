import random
import os
import sys
import subprocess

#this is a rock paper scissor game where the total winner is decided after 5 rounds.

#initialise list
comp_option = ['paper', 'rock', 'scissor']

#choosing random string from the list
computer = random.choice(comp_option)
            
print("\nHello hello!")
print("\nLet's play Paper Rock Scissor!")
print("Play all 5 rounds to see which of us win the whole game!")

#set up variables that will be used inside and outside functions
comp_win = "I win! :D"
user_win = "Congrats you win! :D"
comp_count = 0
user_count = 0
draw_count = 0
i = 1
        
while i <= 5:
    #add argument to the function so Pylance can read these variables
    def restart(user_count, comp_count, draw_count):
        
        while True:
            user_choice = input("Please enter either paper, rock, or scissor: ")
            user = user_choice.lower()

            print(f"You chose {user} and I chose {computer}.")

            if user == computer:
                print ("It's a draw! :O")
                draw_count += 1
                break
            elif user == "paper":
                if computer == "rock":
                    user_count += 1
                    print(user_win)
                    break
                else:
                    comp_count += 1
                    print(comp_win)
                    break
            elif user == "rock":
                if computer == "scissor":
                    print (user_win)
                    user_count += 1
                    break
                else:
                    comp_count += 1
                    print(comp_win)
                    break
            elif user == "scissor":
                if computer == "paper":
                    print(user_win)
                    user_count += 1
                    break
                else:
                    print (comp_win)
                    comp_count += 1
                    break
            else:
                print("It seems you enter the wrong options, or accidentally adding a space. Please try again!")
                continue  
        return user_count, comp_count, draw_count
    
    print (f"\nROUND {i}, START!")
    # Call the function and update the counts accordingly
    user_count, comp_count, draw_count = restart(user_count, comp_count, draw_count)
    i += 1
    
else:
    print (f"From these rounds, you have won {user_count} times while I have won {comp_count} times. And there's {draw_count} times where it's a draw.")
    
    if user_count > comp_count:
        print (f"Congratulations! You win!")
    else:
        print (f"You have lost! Better luck next time!")
    print ("\nThanks for playing!")
    
    user_try = input("\nWould you like to try again? (Y/N): ")
    retry = user_try.upper()
    
    if retry == "Y":
        #restarting the program. Don't forget to import sys os and subprocess first
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])      
    elif retry == "N":
        print ("Alright then, see you next time!")
        quit()
