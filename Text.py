text = "Natural Language Processing Using Python"
words = text.split()
x = [len(word) for word in words]
y = sum(x)
z = y / len(x)
print(y, z)



text = "Natural Language Processing Using Python"
words = text.split()
x = [len(word) for word in words]
y = sum(x)
z = y / len(words)
print(y, z)
