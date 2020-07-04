def playusergame():
    global rate
    file = open(rating, 'r', encoding='utf-8')
    for line in file:
        if line.startswith(name):
            rate = int(line.split()[1])
    file.close()
    print("Okay, let's start\n")
    while x == 0:
        userinput = input()
        import random
        randoption = random.choice(option)
        if userinput == randoption:
            print('There is a draw ({a})'.format(a=randoption))
            rate += 50
        elif userinput in option:
            loselist = option[option.index(userinput) + 1:option.index(userinput) + int((len(option) - 1) / 2) + 1:1]
            for item in option:
                if len(loselist) < int((len(option) - 1) / 2):
                    loselist.append(item)
            if randoption in loselist:
                print('Sorry, but computer chose {a}'.format(a=randoption))
            else:
                print('Well done. Computer chose {a} and failed'.format(a=randoption))
                rate += 100
        elif userinput == '!rating':
            print('Your rating: ', rate)
        elif userinput == '!exit':
            print('Bye!')
            break
        else:
            print('Invalid input')

def playclassicgame():
    global option
    option = ['paper', 'scissors', 'rock']
    playusergame()

rating = 'rating.txt'
x = 0
rate = 0
name = input('Enter your name:')
print('Hello, ', name)
option = input().split(',')
if option[0] == "":
    playclassicgame()
else:
    playusergame()
