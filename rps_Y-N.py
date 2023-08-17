import random
import os
import sys
import subprocess

#this is an endless rock paper scissor, where it keeps asking the player if they want to continue playing until they say no.

#initialise list
comp_option = ['paper', 'rock', 'scissor']

print("\nHello hello!")
print("\nLet's play Paper Rock Scissor!")
print("Play all 5 rounds to see which of us win the whole game!")

#set up variable i before using it.
i = 1

while i <= 5:
    def restart():
        
        while True:
            user_choice = input("Please enter either paper, rock, or scissor: ")
            user = user_choice.lower()

            #choosing random string from the list
            computer = random.choice(comp_option)

            print(f"You chose {user} and I chose {computer}.")

            comp_win = "I win! :D"
            user_win = "Congrats you win! :D"

            if user == computer:
                print ("It's a draw! :O")
                break
            elif user == "paper":
                if computer == "rock":
                    print(user_win)
                    break
                else:
                    print(comp_win)
                    break
            elif user == "rock":
                if computer == "scissor":
                    print (user_win)
                    break
                else:
                    print(comp_win) 
                    break
            elif user == "scissor":
                if computer == "paper":
                    print(user_win)
                    break
                else:
                    print (comp_win)
                    break
            else:
                print("It seems you enter the wrong options, or accidentally adding a space. Please try again!")
                continue  
    
    print (f"\nROUND {i}, START!")
    i += 1
    restart()
    
    user_try = input("\nDo you want to try again? (Y/N): ")
    retry = user_try.upper()
    if retry == "Y": 
        continue #this one was the problem. Should've said continue because when you said restart() it will reset the value and repeat the function again before continuing to "ROUND {i}"
          
    elif retry == "N":
        print ("Thank you for playing!")
        quit()
    else:
        print("Sorry, I do not recognise your input. The program will restart now.")
        #restarting the program. Don't forget to import sys os and subprocess first
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])   
        
'''
what to look up:
    - counting each Loop
    - fix the Round {i} problem
    - I think what's the problem is the function resets the value back to default (1) when it executes.
'''