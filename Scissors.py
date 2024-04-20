def determine_winner(user_choice, computer_choice):
    # Rules dictionary
    rules = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'Spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['Spock', 'paper'],
        'Spock': ['rock', 'scissors']
    }
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in rules[user_choice]:
        return "You win!"
    else:
        return "Computer wins!"

# Prompt user for choice
user_choice = input("Enter your choice (rock, paper, scissors, lizard, Spock): ").lower()

# Generate computer's choice (randomly)
import random
choices = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
computer_choice = random.choice(choices)

print("Computer's choice:", computer_choice)

# Determine the winner
result = determine_winner(user_choice, computer_choice)
print(result)
