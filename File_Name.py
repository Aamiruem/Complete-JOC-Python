file_name = input()
with open(file_name, 'r') as file:
    text = file.read()
    no_of_words = [len(sentence.strip().split()) for sentence in text.split('\n') if sentence.strip()]
    average_length = sum(no_of_words) / len(text)
print('Average sentence length', average_length)
print('Sentences with more than 20 words:')
print(" I am a king of computer science all over universe")
