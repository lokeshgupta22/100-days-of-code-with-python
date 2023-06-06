from coffeemachine_database import menu, resources
import os


def prepare(type, resources):
    reqw = menu[type]["ingredients"]["water"]
    reqm = menu[type]["ingredients"]["milk"]
    reqc = menu[type]["ingredients"]["coffee"]

    totalw = resources["water"]
    totalm = resources["milk"]
    totalc = resources["coffee"]

    totalw = totalw - reqw
    totalm = totalm - reqm
    totalc = totalc - reqc
    if totalc >= 0 and totalm >= 0 and totalw >= 0:
        print("Here is your " + type + " enjoy!")
        resources = {"water": totalw, "milk": totalm, "coffee": totalc}
        return resources
    else:
        if totalw < 0:
            print("Sorry there is not enough water.")
        if totalm < 0:
            print("Sorry there is not enough milk.")
        if totalc < 0:
            print("Sorry there is not enough coffee.")
        print("Money refunded.")


def money(type, r):
    print(f"You need to pay {menu[type]['cost']} dollars.")
    print("Please insert coins!")
    m = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}
    total = 0
    c = 0
    for i in m:
        inp = int(input(f"How many {i}?: "))
        m[i] = inp
    # print(m)
    total = round((m["quarters"]*0.25) + (m["dimes"]*0.10) +
                  (m["nickels"]*0.05) + (m["pennies"]*0.01), 1)
    c = menu[type]["cost"]
    if c == total:
        retres = prepare(type, r)
    elif c > total:
        print("Sorry that's not enough money. Money refunded.")
        retres = r
    elif c < total:
        print(f"Here is ${round(total-c,2)} dollars in change.")
        retres = prepare(type, r)
    return retres


def machine(resources):
    contd = True
    while contd:
        os.system("clear")
        ch = input(
            "What would you like? (espresso -> e/latte -> l/cappucino -> c): ").lower()
        if ch == "report":
            ret = resources
            w = resources["water"]
            m = resources["milk"]
            c = resources["coffee"]
            print(f"Water: {w} ml\nMilk: {m} ml\nCappucino: {c} g")
        elif ch == "e":
            ret = money("espresso", resources)
        elif ch == "l":
            ret = money("latte", resources)
        elif ch == "c":
            ret = money("cappuccino", resources)
        else:
            print("Invalid")
        re = input("Would you like to use the machine again? (y/n): ")
        if re == "y":
            contd = True
            resources = ret
        elif re == "n":
            contd = False
        else:
            print("Invalid")
            contd = False


machine(resources)
