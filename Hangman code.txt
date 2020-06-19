import random
word = ['python', 'java', 'kotlin', 'javascript']
tries = 0
print('HANGMAN\n')
w = random.choice(word)
l = list(w)
m = list(len(l) * "-")
print("".join(m))
indexes = []
for tries in range(8):
    guess = input("Input a letter:")
    if guess in l:
        for i in range(len(m)):
            if l[i] == guess:
                indexes.append(i)
        for ind in indexes:
            m.insert(ind, guess)
            del m[ind+1]
            indexes = []
        if "".join(m).isalpha():
            break
        print('\n')
        print("".join(m))
    else:
        print("No such letter in the word")
        print('\n')
        print("".join(m))
print('\n')
print("Thanks for playing!\nWe'll see how well you did in the next stage")