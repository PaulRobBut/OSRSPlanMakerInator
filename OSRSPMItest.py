## TODO: Ensure all of the project follows the rules of encapsulation
## TODO: Consolidate File, Object, and Method names
## TODO: Complete docs and comments
## TODO: Make it easier to add future Chance Items, such as enhanced crystal keys for example
## Bonus tasks when a Goal has been completed
import OSRSPlanSaver
import OSRSPMIObjects

## Variables
progStateStack = ["Main Menu"]
progNextStates = ["Chance Items", "Inventory", "Main Goals", "Edit"]
userChoice = "" ## User input value
## Key: (Young Impling Jar), (Gourmet Impling Jar), (Eclectic Impling Jar), (Magpie Impling Jar), (Dragon Impling Jar), (Fiyr remains), (Urium Remains), (Ogre Coffin Keys), (Zombie Pirate Keys), (Rogue's Chest), (Grubby Chest)

user = OSRSPMIObjects.User("Test")

## TODO: Move Functions into its own file
## Functions
def setChcArr(user):
    if len(user.realChcArr) > 0:
        user.realChcArr.clear()
    gArrs = OSRSPlanSaver.loadChcArrs()
    bArr = []
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Young Impling Jar", user.chcArr[0], 0, gArrs[0], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Gourmet Impling Jar", user.chcArr[1], 0, gArrs[1], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Eclectic Impling Jar", user.chcArr[2], 0, gArrs[2], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Magpie Impling Jar", user.chcArr[3], 0, gArrs[3], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Dragon Impling Jar", user.chcArr[4], 0, gArrs[4], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Fiyr remains", user.chcArr[5], 0, gArrs[5], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Urium remains", user.chcArr[6], 0, gArrs[6], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Ogre Coffin Key", user.chcArr[7], 0, gArrs[7], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Zombie Pirate Key", user.chcArr[8], 0, gArrs[8], bArr, True))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Rogue's Chest", user.chcArr[9], 0, gArrs[9], bArr, True, "Lockpick"))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Grubby Key", user.chcArr[10], 0, gArrs[10], bArr))

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

def setWantedItems(chc):
    """
    Loops through all of a Chance Item's drops, asking you if they should be set to Good Drops or Bad Drops
    :param chc: Chance Item
    """
    retGood = []
    retBad = []
    ## TODO: consolidate for loops into a single for loop
    ## Which would also mean taking the code form judgeWantItem and putting it here.
    for c in chc.good_items:
        judgeWantItem(retGood, retBad, c)
    for c in chc.bad_items:
        judgeWantItem(retGood, retBad, c)
    chc.good_items = retGood
    chc.bad_items = retBad
    print("Finished sorting for " + chc.name + "!")

def judgeWantItem(rGood, rBad, item):
    uInput = ""
    while uInput != "Good" and uInput != "Bad":
        uInput = input(item + ", Good or Bad? ")
        if uInput == "Good":
            print(item + " is a GOOD drop!")
            rGood.append(item)
        elif uInput == "Bad":
            print(item + " is a BAD drop!")
            rBad.append(item)
        else:
            print("Invalid choice, type Good or Bad, case sensitive.")

def chooseInt(maxVal):
    chooseChc = -1
    try:
        chooseChc = int(input("Choose (0 - " + str(maxVal) + "): "))
    except:
        print("Invalid, that is not an integer.")
    if chooseChc < 0 or chooseChc > maxVal:
        print("Invalid, choice is not between 0 and " + str(maxVal) + ".")
    return chooseChc

def viewChcItems(user):
    uChc = "Yes"
    while uChc == "Yes":
        print("0: Young Impling Jar\n1: Gourmet Impling Jar\n2: Eclectic Impling Jar\n3: Magpie Impling Jar\n4: Dragon Impling Jar\n5: Fiyr remains\n6: Urium Remains\n7: Ogre Coffin Keys\n8: Zombie Pirate Keys\n9: Rogue's Chest\n10: Grubby Chest")
        uChcInt = chooseInt(10)
        print("Good Items")
        print(user.realChcArr[uChcInt].good_items)
        print("Bad Items")
        print(user.realChcArr[uChcInt].bad_items)
        uChc = input("Continue (Yes / No)? ")
        if uChc == "Yes":
            displayChanceItems(user.realChcArr)
    print("Returning, type 'exit' to go to previous menu")

def setState(menuChoice, validChoices):
    ## TODO: This method is a bit of a mess, find a way to truncate it
    ## TODO: Make selections not case-sensitive
    global user
    validChoices.clear()
    if menuChoice == "Main Menu":
        validChoices.append("Chance Items")
        validChoices.append("Inventory")
        validChoices.append("Main Goals")
        validChoices.append("Edit")
    elif menuChoice == "Chance Items":
        ## Leaves a bit too much text, can be consolidated
        displayChanceItems(user.realChcArr)
        viewChcItems(user)
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
        validChoices.append("Set Wanted Drops")
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
    elif menuChoice == "Set Wanted Drops":
        chooseChc = -1
        while chooseChc < 0 or chooseChc > 10:
            ## TODO: This one line is way too long, split it between several lines
            print("Which Chance Item would you like to set the wanted drops to:\n0: Young Impling Jar\n1: Gourmet Impling Jar\n2: Eclectic Impling Jar\n3: Magpie Impling Jar\n4: Dragon Impling Jar\n5: Fiyr remains\n6: Urium Remains\n7: Ogre Coffin Keys\n8: Zombie Pirate Keys\n9: Rogue's Chest\n10: Grubby Chest")
            chooseChc = chooseInt(10)
        setWantedItems(user.realChcArr[chooseChc])
        progStateStack.pop()
        if (len(progStateStack) > 0):
            setState(progStateStack[len(progStateStack) - 1], progNextStates)
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
uName = input("What is your name: ")
if uName == "": uName = "Test"
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