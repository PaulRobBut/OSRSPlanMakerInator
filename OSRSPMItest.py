## TODO: Ensure all of the project follows the rules of encapsulation
## TODO: Consolidate File, Object, and Method names
## TODO: Complete docs and comments
## TODO: Make it easier to add future Chance Items, such as enhanced crystal keys for example
## Bonus tasks when a Goal has been completed
import OSRSPlanSaver
import OSRSPMIObjects
import OSRSPMIFunctions

## Variables
progStateStack = ["Main Menu"]
progNextStates = ["Chance Items", "Inventory", "Main Goals", "Edit"]
userChoice = "" ## User input value
## Key: (Young Impling Jar), (Gourmet Impling Jar), (Eclectic Impling Jar), (Magpie Impling Jar), (Dragon Impling Jar), (Fiyr remains), (Urium Remains), (Ogre Coffin Keys), (Zombie Pirate Keys), (Rogue's Chest), (Grubby Chest)

user = OSRSPMIObjects.User("Test")

def setState(menuChoice, validChoices):
    ## TODO: This method is a bit of a mess, find a way to truncate it
    ## Idea: Make a state tree
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
        OSRSPMIFunctions.displayChanceItems(user.realChcArr)
        OSRSPMIFunctions.viewChcItems(user)
    elif menuChoice == "Inventory":
        OSRSPMIFunctions.displayInventory(user.inventory)
    elif menuChoice == "Main Goals":
        ## TODO: Ability to Add / Clear Goals
        print("\nYour current goals are:")
        for m in user.mainGoals.values():
            OSRSPMIFunctions.displayGoal(m, user.inventory)
        validChoices.append("Add Goal")
        validChoices.append("Clear/Remove Goal")
    elif menuChoice == "Add Goal":
        OSRSPMIFunctions.createMainGoal(user)
    elif menuChoice == "Clear/Remove Goal":
        OSRSPMIFunctions.cleRemGoal(user)
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
        ##TODO: Function to edit a main goal
        print("To be worked on")
    elif menuChoice == "Load Plans":
        user = OSRSPMIObjects.User("Frank", 0, [0,0,0,0,0,0,0,0,0,0,0], [], dict(), dict())
        print(user.name)
        print(len(user.inventory.values()))
        OSRSPMIFunctions.setChcArr(user) ## TODO: One of these setsChcArrs will need to be removed
        OSRSPlanSaver.loadPlan(user)
        OSRSPMIFunctions.setChcArr(user)
    elif menuChoice == "Save Plans":
        OSRSPlanSaver.savePlan(user)
    elif menuChoice == "Set Wanted Drops":
        chooseChc = -1
        while chooseChc < 0 or chooseChc > 10:
            ## TODO: This one line is way too long, split it between several lines
            print("Which Chance Item would you like to set the wanted drops to:\n0: Young Impling Jar\n1: Gourmet Impling Jar\n2: Eclectic Impling Jar\n3: Magpie Impling Jar\n4: Dragon Impling Jar\n5: Fiyr remains\n6: Urium Remains\n7: Ogre Coffin Keys\n8: Zombie Pirate Keys\n9: Rogue's Chest\n10: Grubby Chest")
            chooseChc = OSRSPMIFunctions.chooseInt(10)
        OSRSPMIFunctions.setWantedItems(user.realChcArr[chooseChc])
        progStateStack.pop()
        if (len(progStateStack) > 0):
            setState(progStateStack[len(progStateStack) - 1], progNextStates)
    else:
        print("Construction Zone")

## test = ChanceItem("Baby Impling Jar", 0, 1000, ["Basically", "Nothing"], ["Everything Else"])

## Test Area
# testItem = OSRSPMIObjects.InvenItem("Hat", 5)
# testPlan = OSRSPMIObjects.MainGoal("Rev up those fryers", "For I'm ready for one", [testItem])
# user.inventory[testItem.name] = testItem
# user.mainGoals[testPlan.name] = testPlan

## Program Start
OSRSPMIFunctions.setChcArr(user)
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