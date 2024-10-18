import OSRSPlanSaver

progStateStack = ["Main Menu"]
progNextStates = ["Chance Items", "Inventory", "Main Goals", "Edit"]

## Classes
class ChanceItem():
    """
    Represents a Chance Item
    :param n: Item name (String)
    :param a: Amount of said item you have (Integer)
    :param p: Price of Chance Item (in GP) (Integer)
    :param g: Good Items in drop table (InvenItem Array)
    :param b: Junk items in drop table (InvenItem Array)
    :param pm: Does accessing the drop table require a PK risk? (Boolean)
    :param i: Additional item needed to access drop table (String)
    """
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
    """
    Represents an Inventory Item
    :param n: Item name (String)
    :param a: Amount of item you have (Integer)
    """
    def __init__(self, n, a):
        self.name = n
        self.amount = a

    def compare(self, o): ## o: other item to compare
        self.amount += o.amount
        ## Just in case 
        ## if self.name == o.name:
        ##     return True
        ## else:
        ##     return False

    def printInvenItem(self):
        print(self.name + ": " + str(self.amount))


class MainGoal():
    """
    Represents a Main Goal
    :param n: Title of your Goal (String)
    :param d: Description of Goal (String)
    :param i: Items needed for the Goal (InvenItem Array)
    """
    def __init__(self, n, d, i):
        self.name = n
        self.description = d
        self.neededItems = i

    def printMainGoal(self):
        print(self.name + ": " + self.description)

    def canDoGoal(self, i): ## takes in Player inventory, returns a result depending on if the Player's inventory
                            ## has the required Items
                            ## Key:
                            ## Green: You have all the items in the required amount
                            ## Yellow: You have all the required items, but not the required amounts
                            ## Orange: You have at least one of the required items (quantity not withstanding)
                            ## Red: You have none of the required items
                            ## Returns an int from 0 (red) to 3 (green)
        alo = False ## If there's at least one item in your inventory
        for needIt in self.neededItems:
            if needIt.name not in i:
                if alo:
                    return 1
                else:
                    return 0
            elif needIt.amount > i.get(needIt.name).amount:
                return 2
            alo = True
        return 3
        ## TODO: List items you need
            

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

def displayInventory(inven): ## Displays Every item in your inventory
    print("Printing Inventory: ")
    for i in inven.values():
        i.printInvenItem()
    print()

def displayGoal(goal, inven): ## Displays a single Goal and if you're ready to do it
    c = goal.canDoGoal(inven)
    if (c == 0): c = "Red"
    elif (c == 1): c = "Orange"
    elif (c == 2): c = "Yellow"
    else: c = "Green"
    print(goal.name + ": State: " + c + ", Description: " + goal.description)
    print("Needed Items: ")
    for i in goal.neededItems:
        i.printInvenItem()
    print()

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
inven = dict()
mainGoals = dict()
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

## Test Area
testItem = InvenItem("Bug", 2)
testItemTwo = InvenItem("Bob", 2)
testItemThree = InvenItem("Bob", 3)
testItemFour = InvenItem("Ball", 1)
testPlan = MainGoal("Doot", "Test Goal", [testItem])
testPlanTwo = MainGoal("Poop", "Another Test Goal", [testItemThree])
testPlanThree = MainGoal("Loop", "Yep, another Test", [testItem, testItemFour])
testPlanFour = MainGoal("Hoop", "One Plus One Equals B?!?!?!", [testItemFour])
inven[testItem.name] = testItem
inven[testItemTwo.name] = testItemTwo
mainGoals[testPlan.name] = testPlan
# inven[testItem.name].printInvenItem()
# mainGoals[testPlan.name].printMainGoal()
# displayInventory(inven)
# displayGoal(testPlan, inven)
# print(testItem.name in inven) ## true
# print(testPlan.canDoGoal(inven)) ## Green
# print(testPlanTwo.canDoGoal(inven)) ## Yellow
# print(testPlanThree.canDoGoal(inven)) ## Orange
# print(testPlanFour.canDoGoal(inven)) ## Red
displayInventory(inven)
displayGoal(testPlan, inven)

## Program Start
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