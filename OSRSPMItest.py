## TODO: Ensure all of the project follows the rules of encapsulation
import OSRSPlanSaver
import OSRSPMIObjects

## Variables
progStateStack = ["Main Menu"]
progNextStates = ["Chance Items", "Inventory", "Main Goals", "Edit"]
userChoice = "" ## User input value
chcArr = [0,0,0,0,0,0,0,0,0,0,0] ## Chance Item Array (May need to be worked out)
realChcArr = []
## TODO: Fill out all chance Items with proper information (Default all items to good)
## Key: (Young Impling Jar), (Gourmet Impling Jar), (Eclectic Impling Jar), (Magpie Impling Jar), (Dragon Impling Jar), (Fiyr remains), (Urium Remains), (Ogre Coffin Keys), (Zombie Pirate Keys), (Rogue's Chest), (Grubby Chest)

inven = dict()
mainGoals = dict()
curGP = 0

## Functions
def setChcArr(chc):
    if len(realChcArr) > 0:
        realChcArr.clear()
    realChcArr.append(OSRSPMIObjects.ChanceItem("Young Impling Jar", chc[0], 0, ["Poop"], ["Doo Doo"]))
    realChcArr.append(OSRSPMIObjects.ChanceItem("Gourmet Impling Jar", chc[1], 0, ["Poop"], ["Doo Doo"]))
    realChcArr.append(OSRSPMIObjects.ChanceItem("Eclectic Impling Jar", chc[2], 0, ["Poop"], ["Doo Doo"]))
    realChcArr.append(OSRSPMIObjects.ChanceItem("Magpie Impling Jar", chc[3], 0, ["Poop"], ["Doo Doo"]))
    realChcArr.append(OSRSPMIObjects.ChanceItem("Dragon Impling Jar", chc[4], 0, ["Poop"], ["Doo Doo"]))
    realChcArr.append(OSRSPMIObjects.ChanceItem("Fiyr remains", chc[5], 0, ["Poop"], ["Doo Doo"]))
    realChcArr.append(OSRSPMIObjects.ChanceItem("Urium remains", chc[6], 0, ["Poop"], ["Doo Doo"]))
    realChcArr.append(OSRSPMIObjects.ChanceItem("Ogre Coffin Key", chc[7], 0, ["Poop"], ["Doo Doo"]))
    realChcArr.append(OSRSPMIObjects.ChanceItem("Zombie Pirate Key", chc[8], 0, ["Poop"], ["Doo Doo"], True))
    realChcArr.append(OSRSPMIObjects.ChanceItem("Rogue's Chest", chc[9], 0, ["Poop"], ["Doo Doo"], True, "Lockpick"))
    realChcArr.append(OSRSPMIObjects.ChanceItem("Grubby Key", chc[10], 0, ["Poop"], ["Doo Doo"]))

def displayChanceItems(chc):
    for i in chc:
        i.displayChanceItem()

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
        displayChanceItems(realChcArr)
    elif menuChoice == "Inventory":
        displayInventory(inven)
    elif menuChoice == "Main Goals":
        ## TODO: Ability to Add / Clear Goals
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
        validChoices.append("Adjust Chance Item Quantity")
        validChoices.append("Set Good/Bad Drops")
    elif menuChoice == "Edit Inventory":
        validChoices.append("Add Items")
        validChoices.append("Remove Items")
        validChoices.append("Adjust Items")
    elif menuChoice == "Edit Main Goals":
        ## TODO: Create a seperate method for editing the text of the goals
        print("I'll get back to you on this one")
    elif menuChoice == "Load Plans":
        print("Construction Zone")
    elif menuChoice == "Save Plans":
        OSRSPlanSaver.savePlan(curGP, chcArr, realChcArr, inven, mainGoals)
    else:
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
setChcArr(chcArr)
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