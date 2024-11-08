import OSRSPMIObjects
import OSRSPlanSaver
import random

## TODO: Reorganize these
def setChcArr(user):
    """
    Sets User's Real Chance Item Array based on the simplified Chance Item Array
    :param user: User object
    """
    if len(user.realChcArr) > 0:
        user.realChcArr.clear()
    gArrs = OSRSPlanSaver.loadChcArrs()
    bArr = []
    ## TODO: Price and Profit fields
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Young Impling Jar", user.chcArr[0], 3000, -1700, gArrs[0], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Gourmet Impling Jar", user.chcArr[1], 5000, -3500, gArrs[1], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Eclectic Impling Jar", user.chcArr[2], 6000, -4000, gArrs[2], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Magpie Impling Jar", user.chcArr[3], 33000, -16000, gArrs[3], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Dragon Impling Jar", user.chcArr[4], 530000, -365000, gArrs[4], bArr))
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Fiyr remains", user.chcArr[5], 0, 0, gArrs[5], bArr)) ## Find average profit
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Urium remains", user.chcArr[6], 0, 0, gArrs[6], bArr)) ## Find average profit
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Ogre Coffin Key", user.chcArr[7], 0, 0, gArrs[7], bArr)) ## Find average profit
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Zombie Pirate Key", user.chcArr[8], 0, 0, gArrs[8], bArr, True)) ## Find average profit
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Rogue's Chest", user.chcArr[9], 0, 0, gArrs[9], bArr, True, "Lockpick")) ## Find average profit
    user.realChcArr.append(OSRSPMIObjects.ChanceItem("Grubby Key", user.chcArr[10], 0, 0, gArrs[10], bArr)) ## Find average profit

def displayChanceItems(chc):
    """
    Displays all User's Chance Items to console
    :param chc: User's Real Chance Item Array
    """
    for i in chc:
        i.displayChanceItem()

def displayInventory(inven): ## Displays Every item in your inventory
    """
    Displays User Inventory to console
    :param inven: User's Inventory
    """
    print("\nPrinting Inventory: ")
    for i in inven.values():
        i.printInvenItem()

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

def createInvenItem(user):
    """
    Creates an Inventory Item for the user with their input
    """
    invItName = input("Name of Item: ")
    invItAmnt = chooseInt(2147483647)
    ## TODO: If the item already exists in the user's inventory, add up their amounts.
    user.inventory[invItName] = OSRSPMIObjects.InvenItem(invItName, invItAmnt)

def removeInvenItem(user):
    if len(user.inventory) > 0:
        print(user.inventory.keys())
        delInvIt = None
        while delInvIt == None:
            chsInvIt = input("Enter name of the item in your inventory you want to delete: ")
            if chsInvIt in user.inventory.keys():
                delInvIt = user.inventory[chsInvIt]
            else:
                print("Invalid Selection")
                print(user.inventory.keys())
        ruSure = "norp"
        while ruSure != "yes" and ruSure != "no":
            ruSure = input("Really remove inventory item? (yes / no) ")
            if ruSure == "yes":
                user.inventory.pop(delInvIt.name)
                print("Task Removed")
            elif ruSure == "no":
                print("Task Not Removed")
            else:
                print("Invalid Choice")
    else:
        print("You don't have anything in your inventory")

def createMainGoal(user):
    """
    Creates a Main Goal based on User input
    :param user: User Object
    """
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
            ## TODO: Change the number based removal to a name based one, don't know why I did this in the first place.
            ## This entire section needs to be redone
            print("Enter the number to the given goal: ")
            print(list(user.mainGoals.keys())[0])
            for i in range(len(user.mainGoals.keys())):
                print(str(i) + ": " + str(list(user.mainGoals.keys())[i]) + ": " + str(list(user.mainGoals.values())[i].description))
            chsGoal = chooseInt(len(user.mainGoals.keys()) - 1)
            ## Unclear that you can only enter Clear, Remove or exit, and it's tedious that you have to redo the entire process because of that mistake
            cleRem = input("Clear goal, Remove goal or exit (Case Sensitive)? ")
            if cleRem == "Clear":
                print("Goal Clear!")
                user.mainGoals.pop(list(user.mainGoals.keys())[chsGoal])
                if (len(user.bonusTasks) > 0):
                    user.curTask = user.bonusTasks[random.randint(0, len(user.bonusTasks) - 1)]
                    user.curTask.assignTask()
                    print("Task Assign: " + user.curTask.name)
                    print("Description: " + user.curTask.desc)
                    print(str(user.curTask.set_assign) + " times.")
            elif cleRem == "Remove":
                print("Goal Removed")
                user.mainGoals.pop(list(user.mainGoals.keys())[chsGoal])
            elif cleRem == "exit":
                print("Goals have been unchanged")
            else:
                print("invalid, choice must be Clear, Remove or exit, case sensitive.")
        else:
            print("You have a Bonus Task you need to finish")
    else:
        print("You don't have any Goals to delete")

def addTask(user):
    """
    Lets a user add their own Bonus Task
    :param user: User object
    """
    taskName = input("Task Name: ")
    taskDesc = input("Task Description: ")
    print("How many repetitions (Max: 1000, Min: 1): ")
    taskMax = chooseInt(1000, 1)
    user.bonusTasks.append(OSRSPMIObjects.BonusTask(taskName, taskDesc, taskMax))

def removeTask(user):
    if (len(user.bonusTasks) > 0):
        print("Select the number of the task you want to remove")
        for i in range(len(user.bonusTasks)):
            print(str(i) + ": " + user.bonusTasks[i].name)
        chsTask = chooseInt(len(user.bonusTasks) - 1)
        ruSure = "norp"
        while ruSure != "yes" and ruSure != "no":
            ruSure = input("Really delete task? (yes / no) ")
            if ruSure == "yes":
                user.bonusTasks.remove(user.bonusTasks[chsTask])
                print("Task Removed")
            elif ruSure == "no":
                print("Task Not Removed")
            else:
                print("Invalid Choice")
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