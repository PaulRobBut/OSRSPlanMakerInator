import OSRSPlanSaver

class ChanceItem():
    def __init__(self, n = "Commorb", a = 0, p = 1, g = [], b = []):
        self.name = n
        self.amount = a
        self.price = p
        self.good_items = g
        self.bad_items = b

    def printChanceItem(self):
        print(self.name)
        print(self.amount)
        print(self.price)
        print(self.good_items)
        print(self.bad_items)

progStateStack = ["Main Menu"]
progNextStates = ["Chance Items", "Inventory", "Main Goals", "Edit"]
## 0 = Main Menu
## 1 = Chance Items
## 2 = Inventory
## 3 = Main Goals
## 4 = Edit
## 5 = Edit Chance Items
## 6 = Edit Inventory
## 7 = Edit Main Goals
## 8 = Load Plans
## 9 = Save Plans

## test = ChanceItem("Baby Impling Jar", 0, 1000, ["Basically", "Nothing"], ["Everything Else"])
userChoice = ""
while len(progStateStack) > 0:
    userChoice = input("Say Something: ")
    print(userChoice)
    print(progStateStack.pop())

OSRSPlanSaver.loadPlan()
OSRSPlanSaver.savePlan("Testo!")
OSRSPlanSaver.loadPlan()