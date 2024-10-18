import OSRSPlanSaver
import OSRSPMIObjects

## Variables
progStateStack = ["Main Menu"]
progNextStates = ["Chance Items", "Inventory", "Main Goals", "Edit"]
userChoice = "" ## User input value
chcArr = [0,0,0,0,0,0,0,0,0,0,0] ## Chance Item Array
## Key: (Young Impling Jar), (Gourmet Impling Jar), (Eclectic Impling Jar), (Magpie Impling Jar), (Dragon Impling Jar), (Fiyr remains), (Urium Remains), (Ogre Coffin Keys), (Zombie Pirate Keys), (Rogue's Chest), (Grubby Chest)

inven = dict()
mainGoals = dict()
curGP = 0


## Functions
def displayChanceItems(chc):
    pass

def displayInventory(inven): ## Displays Every item in your inventory
    print("\nPrinting Inventory: ")
    for i in inven.values():
        i.printInvenItem()

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

def setState(menuChoice, validChoices):
    validChoices.clear()
    if menuChoice == "Main Menu":
        validChoices.append("Chance Items")
        validChoices.append("Inventory")
        validChoices.append("Main Goals")
        validChoices.append("Edit")
    elif menuChoice == "Chance Items":
        print("Construction Zone")
    elif menuChoice == "Inventory":
        displayInventory(inven)
    elif menuChoice == "Main Goals":
        print("\nYour current goals are:")
        for m in mainGoals.values():
            displayGoal(m, inven)
    elif menuChoice == "Edit":
        validChoices.append("Edit Chance Items")
        validChoices.append("Edit Inventory")
        validChoices.append("Edit Main Goals")
        validChoices.append("Load Plans")
        validChoices.append("Save Plans")
    elif menuChoice == "Edit Chance Items":
        print("Construction Zone")
    elif menuChoice == "Edit Inventory":
        print("Construction Zone")
    elif menuChoice == "Edit Main Goals":
        print("Construction Zone")
    elif menuChoice == "Load Plans":
        print("Construction Zone")
    elif menuChoice == "Save Plans":
        print("Construction Zone")

## test = ChanceItem("Baby Impling Jar", 0, 1000, ["Basically", "Nothing"], ["Everything Else"])

## Test Area
testItem = OSRSPMIObjects.InvenItem("Bug", 2)
testItemTwo = OSRSPMIObjects.InvenItem("Bob", 2)
testPlan = OSRSPMIObjects.MainGoal("Doot", "Test Goal", [testItem])
inven[testItem.name] = testItem
inven[testItemTwo.name] = testItemTwo
mainGoals[testPlan.name] = testPlan

## Program Start
while len(progStateStack) > 0:
    print("\nYou are here: " + progStateStack[len(progStateStack) - 1])
    print("\nSubmenus: ")
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
            setState(userChoice, progNextStates)
    else:
        progStateStack.pop()
        if (len(progStateStack) > 0):
            setState(progStateStack[len(progStateStack) - 1], progNextStates)