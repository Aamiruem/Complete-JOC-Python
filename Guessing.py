import random

# Step 3: Generate Secret Code
def generate_secret_code():
    return random.randint(1000, 9999)

# Step 2: Display Masked Gun
def display_masked_gun():
    print("Welcome to the Masked Gun game!")
    print("Can you unlock the masked gun by guessing the 4-digit code?")

# Step 1: Implement Game Loop
def game_loop():
    secret_code = generate_secret_code()
    attempts_left = 10
    
    while attempts_left > 0:
        # Step 6: Validate and Compare Guess with Secret Code
        guess = input("Enter your guess (a 4-digit numeric code): ")
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a 4-digit numeric code.")
            continue
        
        guess = int(guess)
        
        if guess == secret_code:
            print("Congratulations! You've unlocked the masked gun!")
            break
        else:
            # Step 4: Provide Feedback and Manage Attempts for Guessing
            print("Incorrect guess. Try again.")
            attempts_left -= 1
            print(f"Attempts left: {attempts_left}")
    
    # Step 5: End Game
    if attempts_left == 0:
        print("Out of attempts. The masked gun remains locked.")

# Start the game
if __name__ == "__main__":
    display_masked_gun()
    game_loop()
