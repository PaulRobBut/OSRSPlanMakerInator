import OSRSPlanSaver

progStateStack = ["Main Menu"]
progNextStates = ["Chance Items", "Inventory", "Main Goals", "Edit"]

## Classes
class ChanceItem():
    def __init__(self, n = "Commorb", a = 0, p = 1, g = [], b = []):
        self.name = n
        self.amount = a
        self.price = p
        self.good_items = g
        self.bad_items = b

    def printChanceItem(self):
        print(self.name)
        print(self.amount)
        print(self.price)
        print(self.good_items)
        print(self.bad_items)

## Functions
def setState(menuChoice, validChoices):
    validChoices.clear()
    print(menuChoice)
    if menuChoice == "Main Menu":
        validChoices.append("Chance Items")
        validChoices.append("Inventory")
        validChoices.append("Main Goals")
        validChoices.append("Edit")
    elif menuChoice == "Edit":
        validChoices.append("Edit Chance Items")
        validChoices.append("Edit Inventory")
        validChoices.append("Edit Main Goals")
        validChoices.append("Load Plans")
        validChoices.append("Save Plans")

## 0 = Main Menu
## 1 = Chance Items
## 2 = Inventory
## 3 = Main Goals
## 4 = Edit
## 5 = Edit Chance Items
## 6 = Edit Inventory
## 7 = Edit Main Goals
## 8 = Load Plans
## 9 = Save Plans

## test = ChanceItem("Baby Impling Jar", 0, 1000, ["Basically", "Nothing"], ["Everything Else"])
userChoice = ""
while len(progStateStack) > 0:
    print("You are here: " + progStateStack[len(progStateStack) - 1])
    print("Submenus: ")
    print("------")
    for i in progNextStates:
        print(i)
    print("------")
    print("Choose one of these, or type 'exit' to go to the previous menu.")
    userChoice = input("-> ")
    if userChoice != "exit":
        if userChoice not in progNextStates:
            print("Invalid Selection")
        else:
            progStateStack.append(userChoice)
            print([progStateStack])
            setState(userChoice, progNextStates)
    else:
        progStateStack.pop()
        if (len(progStateStack) > 0):
            print(progStateStack[len(progStateStack) - 1])
            setState(progStateStack[len(progStateStack) - 1], progNextStates)
    print(userChoice)