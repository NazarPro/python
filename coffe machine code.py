waterst = int(input("Write how many ml of water the coffee machine has:"))
milkst = int(input("Write how many ml of milk the coffee machine has:"))
cofst = int(input("Write how many grams of coffee beans the coffee machine has:"))
amount = int(input('Write how many cups of coffee you will need:'))
water = amount * 200
milk = amount * 50
cof = amount * 15
nwater = waterst / water
nmilk = milkst / milk
ncof = cofst / cof
n = min(nwater, nmilk, ncof)
if int(n) == amount:
    print("Yes, I can make that amount of coffee")
elif int(n) > amount:
    print("Yes, I can make that amount of coffee (and even " + str(int(n) - amount) + " more than that)")
else:
    nwater = waterst / 200
    nmilk = milkst / 50
    ncof = cofst / 15
    n = min(nwater, nmilk, ncof)
    print("No, I can make only " + str(int(n)) + " cups of coffee")





water = 400
milk = 540
cof = 120
cups = 9
money = 550
x = 0
def printstate():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk,  "of milk")
    print(cof, "of coffee beans")
    print(cups, "of disposable cups")
    print("$", money, "of money")
    print()
while x != 1:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "buy":
        coftype = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coftype == "1":
            if water >= 250 and cof >= 16 and cups >= 1 and milk >= 0:
                print("I have resources, making you a coffee!")
                water -= 250
                milk -= 0
                cof -= 16
                cups -= 1
                money += 4
            else:
                if water < 250:
                    print("Sorry, not enough water!")
                    continue
                elif milk < 0:
                    print("Sorry, not enough milk!")
                    continue
                elif cof < 16:
                    print("Sorry, not enough coffee beans!")
                    continue
                elif cups < 1:
                    print("Sorry, not enough cups!")
                    continue
        elif coftype == "2":
            if water >= 350 and cof >= 20 and cups >= 1 and milk >= 75:
                print("I have resources, making you a coffee!")
                water -= 350
                milk -= 75
                cof -= 20
                cups -= 1
                money += 7
            else:
                if water < 350:
                    print("Sorry, not enough water!")
                    continue
                elif milk < 75:
                    print("Sorry, not enough milk!")
                    continue
                elif cof < 20:
                    print("Sorry, not enough coffee beans!")
                    continue
                elif cups < 1:
                    print("Sorry, not enough cups!")
                    continue
        elif coftype == "3":
            if water >= 200 and cof >= 12 and cups >= 1 and milk >= 100:
                print("I have resources, making you a coffee!")
                water -= 200
                milk -= 100
                cof -= 12
                cups -= 1
                money += 6
            else:
                if water < 200:
                    print("Sorry, not enough water!")
                    continue
                elif milk < 100:
                    print("Sorry, not enough milk!")
                    continue
                elif cof < 12:
                    print("Sorry, not enough coffee beans!")
                    continue
                elif cups < 1:
                    print("Sorry, not enough cups!")
                    continue
        elif coftype == "back":
            continue
    elif action == "fill":
        addwater = input("Write how many ml of water do you want to add:\n")
        water += int(addwater)
        addmilk = input("Write how many ml of milk do you want to add:\n")
        milk += int(addmilk)
        addcof = input("Write how many grams of coffee beans do you want to add:\n")
        cof += int(addcof)
        addcups = input("Write how many disposable cups of coffee do you want to add:\n")
        cups += int(addcups)
    elif action == "take":
        print("I gave you $" + str(money))
        money = 0
    elif action =="remaining":
        printstate()
    elif action == "exit":
        x=1