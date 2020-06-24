M = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
xw = 0
ow = 0
zc = 0
def printstate():
    print('---------')
    print('| {on1} {tw1} {th1} |'.format(on1=M[0][0], tw1=M[0][1], th1=M[0][2]))
    print('| {on2} {tw2} {th2} |'.format(on2=M[1][0], tw2=M[1][1], th2=M[1][2]))
    print('| {on3} {tw3} {th3} |'.format(on3=M[2][0], tw3=M[2][1], th3=M[2][2]))
    print('---------')
printstate()

def postx(i, j):
    global zc
    M[3-i][j-1] = 'X'
    zc += 1
    printstate()

def posto(i, j):
    global zc
    M[3-i][j-1] = 'O'
    zc += 1
    printstate()

def check_input():
    data = input('Enter the coordinates:')
    if "".join(data.split()).isdecimal() == False:
        print('You should enter numbers!')
        check_input()
    elif len(data) > 2 and len(data) < 2:
        print('Coordinates should be from 1 to 3!')
        check_input()
    elif int(data.split()[0]) not in range(1, 4) or int(data.split()[1]) not in range(1, 4):
        print('Coordinates should be from 1 to 3!')
        check_input()
    elif M[3 - int(data.split()[1])][int(data.split()[0]) - 1] != ' ':
        print('This cell is occupied! Choose another one!')
        check_input()
    else:
        x, y = data.split()
        if zc % 2 != 0:
            posto(i=int(y), j=int(x))
        else:
            postx(i=int(y), j=int(x))

def checkstate():
    global zc
    if M[0][0] == M[0][1] == M[0][2] == 'X' or M[1][0] == M[1][1] == M[1][2] == 'X' or M[2][0] == M[2][1] == M[2][2] == 'X' or M[0][0] == M[1][0] == M[2][0] == 'X' or M[0][1] == M[1][1] == M[2][1] == 'X' or  M[0][2] == M[1][2] == M[2][2] == 'X' or  M[0][0] == M[1][1] == M[2][2] == 'X' or M[0][2] == M[1][1] == M[2][0] == 'X':
        zc += 10
        print('X wins')
    elif M[0][0] == M[0][1] == M[0][2] == 'O' or M[1][0] == M[1][1] == M[1][2] == 'O' or M[2][0] == M[2][1] == M[2][2] == 'O' or M[0][0] == M[1][0] == M[2][0] == 'O' or M[0][1] == M[1][1] == M[2][1] == 'O' or  M[0][2] == M[1][2] == M[2][2] == 'O' or  M[0][0] == M[1][1] == M[2][2] == 'O' or M[0][2] == M[1][1] == M[2][0] == 'O':
        zc += 10
        print('O wins')
    elif zc == 9:
        zc += 2
        print('Draw')

while zc < 10:
    checkstate()
    if zc >=10:
        break
    check_input()
