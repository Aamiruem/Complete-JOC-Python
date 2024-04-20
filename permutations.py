import random

def get_permutations(word):
    word_list = list(word)
    random.shuffle(word_list)
    shuffled_word = ''.join(word_list)
    return shuffled_word
input_word = "python"
result = get_permutations(input_word)
print(result)
    