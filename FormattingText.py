text = "In reality, programming languages are how programmers express and communicate ideas - and the audience for those ideas is other programmers, not computers. The reason: the computer can take care of itself, but programmers are always working with other programmers, and poorly communicated ideas can cause expensive flops. In fact, ideas expressed in a programming language also often reach the end users of the program - people who will never read or even know about the program, but who nevertheless are affected by it."
sentences = text.split('.')
while '' in sentences:
    sentences.remove('')
print(len(sentences))

words = []
for sentence in sentences:
    words_ = sentence.split(' ')
    words.extend(words_)
print(len(words))

proc_words = []
for word in words:
    if word not in [' ', '']:
        proc_words.append(word)
print(len(proc_words))

u_words = {}
for word in proc_words:
    if word not in u_words:
        u_words[word] = 0
    u_words[word] += 1
print(len(u_words))

# first option
while '' in sentences:
    sentences.remove('')
print(len(sentence))

# second option
words = []
for sentence in sentences:
    words_ = sentence.split(' ')
    words.extend(words_)
print(len(words))

#third option
proc_words = []
for word in words:
    if not (word == ' ' or word == '-'):
        proc_words.append(word)
print(len(proc_words))


#fourth option
u_words = dict = []
for word in proc_words:
    if word not in u_words:
        u_words[word] = 0
    u_words[word] += 1
print(len(u_words))
