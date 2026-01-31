# Rock Paper Scissor

import random

seista = 0
me = 0

print("Welcome to the Rock Paper and Scissor")
start = input("Hello Buddy, I am Seista \nDo you want to play with me? \nEnter your response here: ").lower()

if start == "yes" or start == "y":
    while True:
        option = ["rock", "paper", "scissor"]
        seista_choice = random.choice(option)
    
        user_input = input("(Type Rock/Paper/Scissor: ")
        print(f"Seista choose: {seista_choice}")

        if user_input == "rock" and seista_choice == "scissor":
            print("You Won!")
            me += 1
        elif user_input == "scissor" and seista_choice == "paper":
            print("You Won!")
            me += 1
        elif user_input == "paper" and seista_choice == "rock":
            print("You Won!")
            me += 1
        elif user_input == seista_choice :
            print("It's Tie")
        else:
            print("You Lose")
            seista += 1
        print(f"Your Score: {me}\nSeista Score: {seista}")
        print("-------------------------------------------------\n")
else:
    print("Goodbye")

