import random
import sqlite3
conn = sqlite3.connect('card.s3db')
c = conn.cursor()
c.execute("DROP TABLE card")
c.execute('CREATE TABLE card(id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
active_prog = 1

def acccreation():
    conn = sqlite3.connect('card.s3db')
    c = conn.cursor()
    accnum = [4, 0, 0, 0, 0, 0]
    accnummul2 = []
    acc1 = []
    pin = []
    num = 0
    checksum = 0
    iter = 1
    for i in range(9):
        x = random.randint(0, 9)
        accnum.append(x)
    for z in accnum:
        if iter % 2 != 0:
            accnummul2.append(z * 2)
        else:
            accnummul2.append(z)
        iter += 1
    accnummin9 = [x - 9 if x > 9 else x for x in accnummul2]
    for accn in accnum:
        acc1.append(str(accn))
    for nm in accnummin9:
        num += nm
    for chsum in range(0, 10):
        if (chsum + num) % 10 == 0:
            checksum = chsum
    acc1.append(str(checksum))
    for j in range(0, 4):
        y = random.randint(0, 9)
        pin.append(str(y))
    accnumber = "".join(acc1)
    pinn = "".join(pin)
    print('Your card has been created\nYour card number:')
    print(accnumber)
    print('Your card PIN:')
    print('{d1}{d2}{d3}{d4}'.format(d1=pin[0], d2=pin[1], d3=pin[2], d4=pin[3]))
    accounts = [accnumber, pinn]
    c.execute("INSERT INTO card(number, pin) VALUES (?,?)", accounts)
    conn.commit()
    conn.close()

def login():
    conn = sqlite3.connect('card.s3db')
    c = conn.cursor()
    global active_prog
    log_card = input('Enter your card number:\n')
    log_pin = input('Enter your PIN:\n')
    c.execute("SELECT number FROM card WHERE number = (?)", (log_card,))
    isin = c.fetchone()
    if isin != None:
        c.execute("SELECT pin FROM card WHERE number = (?)", (log_card,))
        card_pin = (c.fetchone()[0])
        if card_pin == log_pin:
            print()
            print('You have successfully logged in!\n')
            while active_prog == 1:
                menu_number = input('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n')
                if menu_number == '0':
                    active_prog = 0
                    conn.close()
                    return
                elif menu_number == '1':
                    c.execute("SELECT balance FROM card WHERE number = (?)", (log_card,))
                    balance = c.fetchone()[0]
                    print()
                    print('Balance: ', balance)
                elif menu_number == '2':
                    add_inc = int(input('Enter income:\n'))
                    c.execute("SELECT balance FROM card WHERE number = (?)", (log_card,))
                    balance = c.fetchone()[0]
                    balance += add_inc
                    c.execute("UPDATE card SET balance = (?) WHERE number = (?)", (balance, log_card,))
                    conn.commit()
                    print('Income was added!')
                elif menu_number == '3':
                    acctrans_num = input('Enter card number:\n')
                    c.execute("SELECT number FROM card WHERE number = (?)", (acctrans_num,))
                    isinfransfer = c.fetchone()
                    acctransdict = []
                    for numbers in acctrans_num:
                        acctransdict.append(int(numbers))
                    acctransdict[0] *= 2
                    acctransdict[2] *= 2
                    acctransdict[4] *= 2
                    acctransdict[6] *= 2
                    acctransdict[8] *= 2
                    acctransdict[10] *= 2
                    acctransdict[12] *= 2
                    acctransdict[14] *= 2
                    newnums = [x if x <= 9 else x - 9 for x in acctransdict ]
                    trchecksum = (newnums[0] + newnums[1] + newnums[2] + newnums[3] + newnums[4] + +newnums[5] + newnums[6] + newnums[7] + newnums[8] + newnums[9] + newnums[10] + newnums[11] + newnums[12] + newnums[13] + newnums[14] + newnums[15])
                    if acctrans_num == log_card:
                        print("You can't transfer money to the same account!")
                    elif trchecksum % 10 != 0:
                        print('Probably you made mistake in the card number. Please try again!')
                    elif isinfransfer != None:
                        transfersum = int(input('Enter how much money you want to transfer:\n'))
                        c.execute("SELECT balance FROM card WHERE number = (?)", (log_card,))
                        balance = c.fetchone()[0]
                        if balance >= transfersum:
                            c.execute("SELECT balance FROM card WHERE number = (?)", (log_card,))
                            balance = c.fetchone()[0]
                            balance -= transfersum
                            c.execute("UPDATE card SET balance = (?) WHERE number = (?)", (balance, log_card,))
                            c.execute("SELECT balance FROM card WHERE number = (?)", (acctrans_num,))
                            balance = c.fetchone()[0]
                            balance += transfersum
                            c.execute("UPDATE card SET balance = (?) WHERE number = (?)", (balance, acctrans_num,))
                            conn.commit()
                            print('Success!')
                        else:
                            print('Not enough money!')
                    else:
                        print('Such a card does not exist.')
                elif menu_number == '4':
                    c.execute("DELETE FROM card WHERE number = (?)", (log_card,))
                    conn.commit()
                    print('The account has been closed!')
                elif menu_number == '5':
                    print()
                    print('You have successfully logged out!')
                    conn.close()
                    break
        else:
            print('Wrong card number or PIN!')
    else:
        print('Wrong card number or PIN!')

while active_prog == 1:
    menu_number = input('1. Create an account\n2. Log into account\n0. Exit\n')
    if menu_number == '0':
        print('Bye!')
        break
    elif menu_number == '1':
        acccreation()
    elif menu_number == '2':
        login()