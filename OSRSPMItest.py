## TODO: Ensure all of the project follows the rules of encapsulation
import OSRSPlanSaver
import OSRSPMIObjects

## Variables
progStateStack = ["Main Menu"]
progNextStates = ["Chance Items", "Inventory", "Main Goals", "Edit"]
userChoice = "" ## User input value
## TODO: Fill out all chance Items with proper information (Default all items to good)
## Key: (Young Impling Jar), (Gourmet Impling Jar), (Eclectic Impling Jar), (Magpie Impling Jar), (Dragon Impling Jar), (Fiyr remains), (Urium Remains), (Ogre Coffin Keys), (Zombie Pirate Keys), (Rogue's Chest), (Grubby Chest)

user = OSRSPMIObjects.User("Test")

## Functions
def setChcArr(user):
    if len(user.realChcArr) > 0:
        user.realChcArr.clear()
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Young Impling Jar", user.chcArr[0], 0, ["Poop"], ["Doo Doo"]))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Gourmet Impling Jar", user.chcArr[1], 0, ["Poop"], ["Doo Doo"]))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Eclectic Impling Jar", user.chcArr[2], 0, ["Poop"], ["Doo Doo"]))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Magpie Impling Jar", user.chcArr[3], 0, ["Poop"], ["Doo Doo"]))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Dragon Impling Jar", user.chcArr[4], 0, ["Poop"], ["Doo Doo"]))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Fiyr remains", user.chcArr[5], 0, ["Poop"], ["Doo Doo"]))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Urium remains", user.chcArr[6], 0, ["Poop"], ["Doo Doo"]))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Ogre Coffin Key", user.chcArr[7], 0, ["Poop"], ["Doo Doo"]))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Zombie Pirate Key", user.chcArr[8], 0, ["Poop"], ["Doo Doo"], True))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Rogue's Chest", user.chcArr[9], 0, ["Poop"], ["Doo Doo"], True, "Lockpick"))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Grubby Key", user.chcArr[10], 0, ["Poop"], ["Doo Doo"]))

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
    global user
    validChoices.clear()
    if menuChoice == "Main Menu":
        validChoices.append("Chance Items")
        validChoices.append("Inventory")
        validChoices.append("Main Goals")
        validChoices.append("Edit")
    elif menuChoice == "Chance Items":
        displayChanceItems(user.realChcArr)
    elif menuChoice == "Inventory":
        displayInventory(user.inventory)
    elif menuChoice == "Main Goals":
        ## TODO: Ability to Add / Clear Goals
        print("\nYour current goals are:")
        for m in user.mainGoals.values():
            displayGoal(m, user.inventory)
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
        user = OSRSPMIObjects.User("Frank", 0, [0,0,0,0,0,0,0,0,0,0,0], [], dict(), dict())
        print(user.name)
        print(len(user.inventory.values()))
        setChcArr(user) ## TODO: One of these setsChcArrs will need to be removed
        OSRSPlanSaver.loadPlan(user)
        setChcArr(user)
    elif menuChoice == "Save Plans":
        OSRSPlanSaver.savePlan(user)
    else:
        print("Construction Zone")

## test = ChanceItem("Baby Impling Jar", 0, 1000, ["Basically", "Nothing"], ["Everything Else"])

## Test Area
testItem = OSRSPMIObjects.InvenItem("Hat", 5)
testPlan = OSRSPMIObjects.MainGoal("Rev up those fryers", "For I'm ready for one", [testItem])
user.inventory[testItem.name] = testItem
user.mainGoals[testPlan.name] = testPlan

## Program Start
setChcArr(user)
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