import random

def monty_hall_extended(num_simulations):
    switch_wins = 0
    stick_wins = 0
    for _ in range(num_simulations):
        # Assign one door to have the car and three doors to have goats
        doors = ['car', 'goat', 'goat', 'goat']
        
        # Randomly shuffle the doors
        random.shuffle(doors)
        
        # Randomly select a door as the player's initial choice
        player_choice = random.randint(0, 3)
        
        # Monty opens one door revealing a goat that is not the player's initial choice
        opened_door = (player_choice + 1) % 4
        while doors[opened_door] == 'car' or opened_door == player_choice:
            opened_door = (opened_door + 1) % 4
        
        # Switch the player's choice to the remaining unopened door
        remaining_doors = set(range(4)) - {player_choice, opened_door}
        switched_choice = remaining_doors.pop()
        
        # Check if the switched choice is a win
        if doors[switched_choice] == 'car':
            switch_wins += 1
        
        # Check if the initial choice is a win
        if doors[player_choice] == 'car':
            stick_wins += 1
    
    switch_probability = switch_wins / num_simulations
    stick_probability = stick_wins / num_simulations
    
    return switch_probability, stick_probability

# Run the simulation
num_simulations = 100000
switch_prob, stick_prob = monty_hall_extended(num_simulations)

print("Probability of winning by switching:", switch_prob)
print("Probability of winning by sticking:", stick_prob)
