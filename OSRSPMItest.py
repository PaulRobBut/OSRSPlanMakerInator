import OSRSPlanSaver

progStateStack = ["Main Menu"]
progNextStates = ["Chance Items", "Inventory", "Main Goals", "Edit"]

## Classes
class ChanceItem():
    def __init__(self, n = "Commorb", a = 0, p = 1, g = [], b = [], pk = False, i = "None"):
        self.name = n
        self.amount = a
        self.price = p
        self.good_items = g
        self.bad_items = b
        self.pkRisk = pk
        self.itemNeeded = i

    def printChanceItem(self):
        print(self.name)
        print(self.amount)
        print(self.price)
        print(self.good_items)
        print(self.bad_items)
        print(self.pkRisk)
        print(self.itemNeeded)

class InvenItem():
    def __init__(self, k, n, a):
        self.key = k
        self.name = n
        self.amount = a

    def compare(self, o): ## o: other item to compare
        if self.name == o.name:
            self.amount += o.amount
            return True
        else:
            return False

    def printInvenItem(self):
        print(self.name + " " + str(self.amount))


class MainGoal():
    def __init__(self, k, n, d):
        self.key = k
        self.name = n
        self.description = d

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

## Variables
userChoice = "" ## User input value
chcArr = [0,0,0,0,0,0,0,0,0,0,0] ## Chance Item Array
## Key: (Young Impling Jar), (Gourmet Impling Jar), (Eclectic Impling Jar), (Magpie Impling Jar), (Dragon Impling Jar), (Fiyr remains), (Urium Remains), (Ogre Coffin Keys), (Zombie Pirate Keys), (Rogue's Chest), (Grubby Chest)

## test = ChanceItem("Baby Impling Jar", 0, 1000, ["Basically", "Nothing"], ["Everything Else"])

## Testing Inventory items and comparisons
## test = InvenItem(0, "Bug", 2)
## test.printInvenItem()
## testTwo = InvenItem(0, "Book", 3)
## print(test.compare(testTwo))
## testTwo = InvenItem(0, "Bug", 3)
## print(test.compare(testTwo))
## test.printInvenItem()

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