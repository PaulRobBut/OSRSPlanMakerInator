import os

def savePlan(gp, c, rc, i, goals): ##GP, chcArray, realChcArray, Inventory, Goals
    """
    Saves Plan to a .txt file
    :param g: Current Goals
    """
    saveLines = []
    saveLines.append("(Current GP): " + str(gp) + "\n")
    saveLines.append("")
    for ch in c:
        saveLines[1] += (str(ch) + ":")
    saveLines[1] = saveLines[1][:-1] + "\n"
    for ch in rc:
        saveLines.append("") ## Good Items
        saveLines.append("") ## Bad Items
        for g in ch.good_items:
            saveLines[-2] += (g + ":")
        saveLines[-2] = saveLines[-2][:-1] + "\n"
        for b in ch.bad_items:
            saveLines[-1] += (b + ":")
        saveLines[-1] = saveLines[-1][:-1] + "\n"
    saveLines.append("FLAG Inventory\n")
    for it in i.values():
        saveLines.append(it.name + ":" + str(it.amount) + "\n")
    saveLines.append("FLAG Goals\n")
    for gl in goals.values():
        saveLines.append(gl.name + ":" + gl.description + "\n")
        saveLines.append("")
        for it in gl.neededItems:
            saveLines[-1] += (it.name + "=" + str(it.amount) + ":")
        saveLines[-1] = saveLines[-1][:-1] + "\n"
    useFil = "planTest.txt"
    with open(useFil, "w") as s:
        s.writelines(saveLines)

def loadPlan():
    """
    Loads Plan from file
    """
    loadedLines = []
    useFil = "planTest.txt"
    with open(useFil, "r") as l:
        for ll in l:
            loadedLines.append(ll)
    print("File contents: ")
    for ll in loadedLines:
        print(ll)