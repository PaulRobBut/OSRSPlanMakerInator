import os
from OSRSPMIObjects import InvenItem, MainGoal

def savePlan(user): ##GP, chcArray, realChcArray, Inventory, Goals
    """
    Saves Plan to a .txt file
    :param user: Current User
    """
    saveLines = []
    saveLines.append(user.name + " (Current GP): " + str(user.gpTotal) + "\n")
    saveLines.append("")
    for ch in user.chcArr:
        saveLines[1] += (str(ch) + ":")
    saveLines[1] = saveLines[1][:-1] + "\n"
    for ch in user.realChcArr:
        saveLines.append("") ## Good Items
        saveLines.append("") ## Bad Items
        for g in ch.good_items:
            saveLines[-2] += (g + ":")
        saveLines[-2] = saveLines[-2][:-1] + "\n"
        for b in ch.bad_items:
            saveLines[-1] += (b + ":")
        saveLines[-1] = saveLines[-1][:-1] + "\n"
    saveLines.append("FLAG Inventory\n")
    for it in user.inventory.values():
        saveLines.append(it.name + ":" + str(it.amount) + "\n")
    saveLines.append("FLAG Goals\n")
    for gl in user.mainGoals.values():
        saveLines.append(gl.name + ":" + gl.description + "\n")
        saveLines.append("")
        for it in gl.neededItems:
            saveLines[-1] += (it.name + "=" + str(it.amount) + ":")
        saveLines[-1] = saveLines[-1][:-1] + "\n"
    useFil = "plan" + user.name + ".txt"
    with open(useFil, "w") as s:
        s.writelines(saveLines)
    print("Save Successful!")

def loadPlan(user):
    """
    Loads Plan from file
    """
    loadedLines = []
    useFil = "plan" + user.name + ".txt"
    with open(useFil, "r") as l:
        for ll in l:
            loadedLines.append(ll)
    print("File contents: ")
    curFlag = "User and Chance Items"
    lineNum = 0
    lineBool = True
    addGoal = ""
    for ll in loadedLines:
        ## Maybe all the numLines should be condensed to one onitial split?
        ll = ll[:-1]
        if ll[:4] == "FLAG" and lineNum != 0:
            curFlag = ll[5:]
            lineBool = True
            print("Flag Alert: " + curFlag)
            next
        elif curFlag == "Inventory":
            thirdLine = ll.split(':')
            addItem = InvenItem(thirdLine[0], int(thirdLine[1]))
            user.inventory[thirdLine[0]] = addItem
        elif curFlag == "Goals":
            print()
            if lineBool == True: 
                fourthLine = ll.split(':')
                addGoal = MainGoal(fourthLine[0], fourthLine[1], [])
                lineBool = False
            else: 
                fifthLine = ll.split(':')
                for i in fifthLine:
                    gItem = i.split('=')
                    addGoalItem = InvenItem(gItem[0], int(gItem[1]))
                    addGoal.neededItems.append(addGoalItem)
                user.mainGoals[addGoal.name] = addGoal
                lineBool = True
        else:
            print()
            if lineNum == 0: 
                firstLine = ll.split(' (Current GP): ')
                user.name = firstLine[0]
                print("Name: " + firstLine[0])
                user.gpTotal = int(firstLine[1])
                print("GP: " + firstLine[1])
            elif lineNum == 1: 
                print(ll)
                secondLine = ll.split(':')
                print(secondLine)
                for sl in range(len(secondLine)):
                    user.chcArr[sl] = int(secondLine[sl])
            else:
                rcInd = int((lineNum - 2) / 2)
                print(rcInd)
                if lineNum % 2 == 0:
                    print("Good: " + ll)
                    user.realChcArr[rcInd].good_items = ll.split(":")
                else:
                    print("Bad: " + ll)
                    user.realChcArr[rcInd].bad_items = ll.split(":")
        lineNum += 1
    print("Finished loading " + str(lineNum) + " lines!")

def hasFile(userName):
    savedPlans = getFileUserNames()
    if userName in savedPlans:
        return True
    else:
        return False
    
def getFileUserNames():
    savedPlans = []
    for x in os.listdir():
        if x in os.listdir():
            if x.startswith("plan") and x.endswith(".txt"):
                savedPlans.append(x[4:len(x) - 4])
    return savedPlans

def loadChcArrs():
    dropStrArr = []
    useFil = "chcDrops.txt"
    with open(useFil, "r") as l:
        for ll in l:
            dropStrArr.append(ll[:-1].split(", "))
    return dropStrArr