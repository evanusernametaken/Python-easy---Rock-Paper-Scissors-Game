#Rock, Paper, Scissors Game
#The user plays against the computer, which randomly selects rock, paper, or scissors.
import random
def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'exit' to quit the game.")
    
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")
rock_paper_scissors()
