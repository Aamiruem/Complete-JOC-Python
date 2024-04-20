import random
def genetic_evolution(binary_string):
    mutation_probability = 0.1
    evolved_string = ""
    for bit in binary_string:
        if random.random() < mutation_probability:
                evolved_string += "1" if bit == "0" else "0"
        else:
            evolved_string += bit
    return evolved_string
initial_string = "000000000"
result = genetic_evolution(initial_string)
print(result)
