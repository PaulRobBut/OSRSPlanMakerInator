## TODO: Ensure all of the project follows the rules of encapsulation
## TODO: Consolidate File, Object, and Method names
## TODO: Complete comments
## TODO: Make it easier to add future Chance Items, such as enhanced crystal keys for example
## TODO: Yes/No Prompts need inconsistent capitalization
## TODO: Options in the Chance Item section to view and set Wanted Clue Drops
## Bonus tasks when a Goal has been completed
import OSRSPlanSaver
import OSRSPMIObjects
import OSRSPMIFunctions

## Variables
progStateStack = ["Main Menu"]
stateMap = OSRSPlanSaver.loadStateMap()
progNextStates = stateMap[progStateStack[0]]
userChoice = "" ## User input value
## Key: (Young Impling Jar), (Gourmet Impling Jar), (Eclectic Impling Jar), (Magpie Impling Jar), (Dragon Impling Jar), (Fiyr remains), (Urium Remains), (Ogre Coffin Keys), (Zombie Pirate Keys), (Rogue's Chest), (Grubby Chest)

user = OSRSPMIObjects.User("Test")

def setState(menuChoice):
    """
    Sets state of the program based on what the user chooses, and if they are able to
    :param menuChoice: User's chosen next state
    :param validChoices: Acceptable next states the user can choose
    """
    ## TODO: This method is a bit of a mess, find a way to truncate it
    ## Idea: Make a state tree
    ## TODO: Make selections not case-sensitive
    global user
    ## Main Menu
    if menuChoice == "Chance Items":
        ## Leaves a bit too much text, can be consolidated
        OSRSPMIFunctions.displayChanceItems(user.realChcArr)
        OSRSPMIFunctions.viewChcItems(user)
    elif menuChoice == "Inventory":
        OSRSPMIFunctions.displayInventory(user.inventory)
    ## Main Goals
    elif menuChoice == "Add Goal":
        OSRSPMIFunctions.createMainGoal(user)
    elif menuChoice == "View Goals":
        OSRSPMIFunctions.viewGoals(user)
    elif menuChoice == "Clear/Remove Goal":
        OSRSPMIFunctions.cleRemGoal(user)
    elif menuChoice == "Add Bonus Task":
        OSRSPMIFunctions.addTask(user)
    elif menuChoice == "Remove Bonus Task":
        OSRSPMIFunctions.removeTask(user)
    elif menuChoice == "Increment Bonus Task":
        OSRSPMIFunctions.incTask(user)
    elif menuChoice == "Cancel Current Bonus Task":
        ## TODO: A similar bit of code is in the remove task function, may need to be its own function
        ruSure = "norp"
        while ruSure != "yes" and ruSure != "no":
            ruSure = input("Are you sure? (yes / no) ")
            if ruSure == "yes":
                user.curTask = None
                print("Task Cancelled")
            elif ruSure == "no":
                print("Task Maintained")
            else:
                print("Invalid Choice")
    ## Edit
    elif menuChoice == "Edit Main Goals":
        ##TODO: Function to edit a main goal
        print("To be worked on")
    elif menuChoice == "Load Plans":
        savedFiles = OSRSPlanSaver.getFileUserNames()
        print("Load one of these? " + str(savedFiles))
        chsName = input("Enter Name: ")
        if chsName in savedFiles:
            user = OSRSPMIObjects.User(chsName)
            OSRSPMIFunctions.setChcArr(user) ## TODO: One of these setsChcArrs will need to be removed
            OSRSPlanSaver.loadPlan(user)
            OSRSPMIFunctions.setChcArr(user)
        else:
            print("Invalid Name")
    elif menuChoice == "Save Plans":
        OSRSPlanSaver.savePlan(user)
    ## Edit Chance Items
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
    elif menuChoice == "Adjust Chance Item Quantity":
        ## TODO: Loop this
        chsChcIt = OSRSPMIFunctions.selectByNum(user.realChcArr)
        ## TODO: Show how much of that item you already have, and add a print statement telling user that they're setting the Chance Item's quantity to that value
        chsChcAm = OSRSPMIFunctions.chooseInt(2147483647)
        ChcInd = user.realChcArr.index(chsChcIt)
        user.realChcArr[ChcInd].amount = chsChcAm
        user.chcArr[ChcInd] = chsChcAm
        print("Amount adjusted!")
    ## Edit Inventory
    elif menuChoice == "Add Item":
        OSRSPMIFunctions.createInvenItem(user)
    elif menuChoice == "Remove Item":
        OSRSPMIFunctions.removeInvenItem(user)
    ## End
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
user.name = uName
if OSRSPlanSaver.hasFile(uName):
    OSRSPlanSaver.loadPlan(user)
    OSRSPMIFunctions.setChcArr(user)
    print("A file with that name exists! It has been loaded!")
else:
    print("Creating new plan, remember to save your plan in the Edit menu!")
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
            if userChoice in stateMap.keys():
                progNextStates = stateMap[userChoice]
            else:
                progNextStates = []
            setState(userChoice)
    else:
        progStateStack.pop()
        if (len(progStateStack) > 0):
            setState(progStateStack[len(progStateStack) - 1])
            progNextStates = stateMap[progStateStack[-1]]