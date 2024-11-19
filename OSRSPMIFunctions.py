import OSRSPMIObjects
import OSRSPlanSaver
import random

## TODO: Reorganize these
## General Functions
def chooseInt(maxVal, minVal = 0):
    """
    Allows a user to choose an int value between two values
    :param maxVal: Maximum value you can choose
    :param minVal: Minimum value you can choose (default 0)
    """
    ## TODO: Add an escape function in case a user wants to go back
    chooseChc = -1
    while chooseChc < 0:
        try:
            chooseChc = int(input("Choose (" + str(minVal) + " - " + str(maxVal) + "): "))
        except:
            print("Invalid, that is not an integer.")
        if chooseChc < minVal or chooseChc > maxVal:
            print("Invalid, choice is not between 0 and " + str(maxVal) + ".")
            chooseChc = -1
    return chooseChc

def selectByNum(selArr):
    """
    Allows a user to select an option from a list by entering a number
    :param selArr: Array to be selected from
    """
    printWhat = ""
    if isinstance(selArr[0], OSRSPMIObjects.BonusTask) or isinstance(selArr[0], OSRSPMIObjects.ChanceItem):
        printWhat = "name"
    for i in range(len(selArr)):
        if printWhat == "name":
            print(str(i) + ": " + str(selArr[i].name))
        else:
            print(str(i) + ": " + str(selArr[i]))
    chsGoal = chooseInt(len(selArr) - 1)
    return selArr[chsGoal]

def selectByName(selMap):
    """
    Allows a user to select an item from a map that uses a string-based key
    :param selMap: Map to be selected from
    """
    for k in selMap.keys():
        ## TODO: This may need to be tightened up
        if isinstance(selMap[k], OSRSPMIObjects.MainGoal):
            print(str(k) + ": " + str(selMap[k].description))
        elif isinstance(selMap[k], OSRSPMIObjects.InvenItem):
            print(str(k) + ": " + str(selMap[k].amount))
        else: 
            print(str(k) + ": " + str(selMap[k]))
    chsKey = ""
    while chsKey not in selMap.keys() or chsKey != "exit":
        chsKey = input("Choose a key: ")
        if chsKey == "exit":
            break
        elif chsKey not in selMap.keys():
            print("Invalid choice, please choose from these: ")
            print(selMap.keys())
        else:
            return selMap[chsKey]
        
def removeFrom(keyVal, collField):
    """
    Removes a value from a collection, if the user wants it gone
    :param keyVal: key to the collection for the item to be removed (make sure it's an int when collField is a list)
    :param collField: collection to be removed from
    """
    ruSure = "norp"
    while ruSure != "yes" and ruSure != "no":
        ruSure = input("Are you sure you want it removed? (yes / no) ")
        if ruSure == "yes":
            collField.pop(keyVal)
            print("Item Removed")
        elif ruSure == "no":
            print("Item Not Removed")
        else:
            print("Invalid Choice")

## Chance Item Functions
def setChcArr(user):
    """
    Sets User's Real Chance Item Array based on the simplified Chance Item Array
    :param user: User object
    """
    if len(user.realChcArr) > 0:
        user.realChcArr.clear()
    gArrs = OSRSPlanSaver.loadChcArrs()
    bArr = []
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Young Impling Jar", user.chcArr[0], 3000, -1700, gArrs[0], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Gourmet Impling Jar", user.chcArr[1], 5000, -3500, gArrs[1], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Eclectic Impling Jar", user.chcArr[2], 6000, -4000, gArrs[2], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Magpie Impling Jar", user.chcArr[3], 33000, -16000, gArrs[3], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Dragon Impling Jar", user.chcArr[4], 530000, -365000, gArrs[4], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Fiyr remains", user.chcArr[5], 6000, 1800, gArrs[5], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Urium remains", user.chcArr[6], 6000, 5000, gArrs[6], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Ogre Coffin Key", user.chcArr[7], 3000, 1100, gArrs[7], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Zombie Pirate Key", user.chcArr[8], 18000, 4000, gArrs[8], bArr, True))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Rogue's Chest", user.chcArr[9], 0, 3600, gArrs[9], bArr, True, "Lockpick"))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Grubby Key", user.chcArr[10], 44000, 8000, gArrs[10], bArr))

def displayChanceItems(chc):
    """
    Displays all User's Chance Items to console
    :param chc: User's Real Chance Item Array
    """
    for i in chc:
        i.displayChanceItem()

def setWantedItems(chc):
    """
    Loops through all of a Chance Item's drops, asking you if they should be set to Good Drops or Bad Drops
    :param chc: Chance Item
    """
    retGood = []
    retBad = []
    ## TODO: consolidate for loops into a single for loop
    ## Which would also mean taking the code form judgeWantItem and putting it here.
    ## TODO: set the good/bad arrays from Fiyr/Urium remains to the same list, as they're the same drop table
    for c in chc.good_items:
        judgeWantItem(retGood, retBad, c)
    for c in chc.bad_items:
        judgeWantItem(retGood, retBad, c)
    chc.good_items = retGood
    chc.bad_items = retBad
    print("Finished sorting for " + chc.name + "!")

def judgeWantItem(rGood, rBad, item):
    """
    Sets a Chance Item's good and bad drops
    :param rGood: Chance Item's Good drops
    :param rBad: Chance Item's Bad drops
    :param item: Chance Item to judge the drops of
    """
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

def viewChcItems(user):
    """
    Semi-state for when a user is looking at Chance Items, keeping them here until they decide to leave
    :param user: User Object
    """
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

## Inventory Functions
def displayInventory(inven): ## Displays Every item in your inventory
    """
    Displays User Inventory to console
    :param inven: User's Inventory
    """
    print("\nPrinting Inventory: ")
    for i in inven.values():
        i.printInvenItem()

def createInvenItem(user):
    """
    Creates an Inventory Item for the user with their input
    """
    ## TODO: Failsafe to stop people from starting their Item names with 'FLAG'
    invItName = input("Name of Item: ")
    invItAmnt = chooseInt(2147483647)
    ## TODO: If the item already exists in the user's inventory, add up their amounts.
    user.inventory[invItName] = OSRSPMIObjects.InvenItem(invItName, invItAmnt)

def removeInvenItem(user):
    if len(user.inventory) > 0:
        print(user.inventory.keys())
        delInvIt = selectByName(user.inventory)
        ## Escape code for 'exit' goes here
        removeFrom(delInvIt.name, user.inventory)
    else:
        print("You don't have anything in your inventory")

## Main Goal Functions
def displayGoal(goal, inven): ## Displays a single Goal and if you're ready to do it
    """
    Displays a single Goal to the console, and if you have the items to complete it
    :param goal: indiviual Main Goal to print
    :param inven: User's Inventory
    """
    c = goal.canDoGoal(inven)
    if (c == 0): c = "Red"
    elif (c == 1): c = "Orange"
    elif (c == 2): c = "Yellow"
    else: c = "Green"
    print(goal.name + ": State: " + c + ", Description: " + goal.description)
    print("Needed Items: ")
    for i in goal.neededItems:
        i.printInvenItem()

def createMainGoal(user):
    """
    Creates a Main Goal based on User input
    :param user: User Object
    """
    ## TODO: Failsafe to stop people from starting their Goal names with 'FLAG'
    goalName = input("Name of Goal: ")
    goalDesc = input("Description of Goal: ")
    goalNeedIts = []
    needsMoreItem = "Yes"
    while needsMoreItem == "Yes":
        needsMoreItem = input("Needs another item (Yes/No Case Sensitive): ")
        if needsMoreItem == "Yes":
            itNam = input("Item Name: ")
            itQuan = chooseInt(2147483647, 1)
            goalNeedIts.append(OSRSPMIObjects.InvenItem(itNam, itQuan))
        elif needsMoreItem != "Yes" and needsMoreItem != "No":
            needsMoreItem = "Yes"
            print("Invalid, Type Yes or No, case sensitive")
    user.mainGoals[goalName] = OSRSPMIObjects.MainGoal(goalName, goalDesc, goalNeedIts)

def viewGoals(user):
    for g in user.mainGoals.values():
        displayGoal(g, user.inventory)

def cleRemGoal(user):
    """
    Clears or Removes a goal from a User's Goal list
    :param user: User Object
    """
    if len(user.mainGoals.keys()) > 0:
        if user.curTask == None:
            chsGoal = selectByName(user.mainGoals)
            ## Escape code for 'exit' goes here
            ## Unclear that you can only enter Clear, Remove or exit, and it's tedious that you have to redo the entire process because of that mistake
            cleRem = input("Clear, Remove or exit (Case Sensitive)? ")
            if cleRem == "Clear":
                print("Goal Clear!")
                user.mainGoals.pop(chsGoal.name)
                if (len(user.bonusTasks) > 0):
                    user.curTask = user.bonusTasks[random.randint(0, len(user.bonusTasks) - 1)]
                    user.curTask.assignTask()
                    print("Task Assign: " + user.curTask.name)
                    print("Description: " + user.curTask.desc)
                    print(str(user.curTask.set_assign) + " times.")
            elif cleRem == "Remove":
                removeFrom(chsGoal.name, user.mainGoals)
            elif cleRem == "exit":
                print("Goals have been unchanged")
            else:
                print("invalid, choice must be Clear, Remove or exit, case sensitive.")
        else:
            print("You have a Bonus Task you need to finish")
    else:
        print("You don't have any Goals to delete")

def adjNeedIts(user):
    """
    Lets the user adjust the needed items of a desired Goal
    :param user: User Object
    """
    getGoal = selectByName(user.mainGoals)
    for i in getGoal.neededItems:
        i.printInvenItem()
        goalItOpt = ""
        while goalItOpt == "":
            goalItOpt = input("Keep Item? (Yes, No, Change Name, Change Amount) ")
            if goalItOpt == "Yes":
                pass
            elif goalItOpt == "No":
                getGoal.neededItems.remove(i)
            elif goalItOpt == "Change Name":
                reNam = input("Rename to: ")
                i.name = reNam
                goalItOpt = ""
            elif goalItOpt == "Change Amount":
                print("New amount: ")
                reAmo = chooseInt(2147483647)
                i.amount = reAmo
                goalItOpt = ""
            else:
                print("Invalid selection, choice must be Yes, No, Change Name or Change Amount (case sensitive)")
                goalItOpt = ""
    addIt = ""
    while addIt == "":
        addIt = input("Add another Item? (Yes, No) ")
        if addIt == "Yes":
            addItNam = input("Item Name: ")
            print("Item Amount: ")
            addItAmo = chooseInt(2147483647)
            getGoal.neededItems.append(OSRSPMIObjects.InvenItem(addItNam, addItAmo))
            print("Item Added!")
            addIt = ""
        elif addIt == "No":
            pass
        else:
            print("Invalid selection, choice must be Yes or No (case sensitive)")
            addIt = ""

def addTask(user):
    """
    Lets a user add their own Bonus Task
    :param user: User object
    """
    ## TODO: Failsafe to keep people from giving different bonus tasks the same name
    ## TODO: Failsafe to stop people from starting their task names with 'FLAG'
    taskName = input("Task Name: ")
    taskDesc = input("Task Description: ")
    print("How many repetitions (Max: 1000, Min: 1): ")
    taskMax = chooseInt(1000, 1)
    user.bonusTasks.append(OSRSPMIObjects.BonusTask(taskName, taskDesc, taskMax))

def removeTask(user):
    if (len(user.bonusTasks) > 0):
        print("Select the number of the task you want to remove")
        chsTask = selectByNum(user.bonusTasks)
        ## Escape code for 'exit' goes here
        removeFrom(user.bonusTasks.index(chsTask), user.bonusTasks)
    else:
        print("You don't have any Bonus Tasks")

def incTask(user):
    if user.curTask != None:
        doingTask = "Yes"
        while doingTask == "Yes":
            doingTask = input("Press Enter to increment task, type 'exit' (case sensitive) to stop")
            if doingTask != "exit":
                if user.curTask.incrementTask() == True:
                    user.curTask = None
                else:
                    user.curTask.printCurTask()
                    doingTask = "Yes"
        print("Returning, type 'exit' to go back")
    else:
        print("You don't have a current Bonus Task assigned")