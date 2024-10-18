import os

def savePlan(g):
    """
    Saves Plan to a .txt file
    :param g: Current Goals
    """
    print(g)
    useFil = "planTest.txt"
    with open(useFil, "w") as s:
        s.write(g)

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