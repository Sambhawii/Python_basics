import random

options = ["Rock", "Paper", "Scissors"]


player_choice = input("Choose Rock, Paper, or Scissors: ")
computer_choice = random.choice(options)
    

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "Rock":
    if computer_choice == "Paper":
        print("You lose!")
    else:
        print("You win!")
elif player_choice == "Paper":
    if computer_choice == "Scissors":
         print("You lose!")
    else:
        print("You win!")
elif player_choice == "Scissors":
    if computer_choice == "Rock":
        print("You lose!")
    else:
        print("You win!")
else:
    print("Invalid input. Please enter either Rock, Paper, or Scissors.")

