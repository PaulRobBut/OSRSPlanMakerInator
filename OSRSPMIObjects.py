import random
## TODO: Give every object their own overriden print function
## Classes
class User(): ##GP, chcArray, realChcArray, Inventory, Goals
    """
    Represents the User's plan information
    :param n: Player Name (String)
    :param gp: Total GP (Integer)
    :param c: Chance Item Array (Integer array)
    :param rc: Real Chance Item Array (Chance Item Array)
    :param i: Inventory (InvenItem Dictionary)
    :param g: Main Goals (MainGoal Dictionary)
    """
    def __init__(self, n, gp = 0, c = [0,0,0,0,0,0,0,0,0,0,0], rc = [], i = dict(), g = dict(), ct = None, bt = []):
        self.name = n
        self.gpTotal = gp
        self.chcArr = c
        self.realChcArr = rc
        self.inventory = i
        self.mainGoals = g
        self.curTask = ct
        self.bonusTasks = bt

## TODO: More fields
## Clue drop percent: chances of dropping a clue
## Profit: Average amount of GP gained/lost per item
class ChanceItem():
    """
    Represents a Chance Item
    :param n: Item name (String)
    :param a: Amount of said item you have (Integer)
    :param p: Price of Chance Item (in GP) (Integer)
    :param pro: Average profit of Chance Item (Integer)
    :param g: Good Items in drop table (String Array)
    :param b: Junk items in drop table (String Array)
    :param pm: Does accessing the drop table require a PK risk? (Boolean)
    :param i: Additional item needed to access drop table (String)
    """
    ## TODO: general Profit field
    def __init__(self, n = "Commorb", a = 0, p = 1, pro = 0, g = [], b = [], pk = False, i = "None",):
        self.name = n
        self.amount = a
        self.price = p
        self.profit = pro
        self.good_items = g
        self.bad_items = b
        self.pkRisk = pk
        self.itemNeeded = i

    def printChanceItem(self):
        print(self.name)
        print(self.amount)
        print(self.price)
        print(self.profit)
        print(self.good_items)
        print(self.bad_items)
        print(self.pkRisk)
        print(self.itemNeeded)

    ## TODO: Realign print, aligning sections to columns via tabbing
    def displayChanceItem(self):
        print(self.name + ", (" + str(self.price) + " GP ea, Profit: " + str(self.profit) + " GP ea, Needed Item: " + self.itemNeeded + ", PK Risk: " + str(self.pkRisk) + "): " + str(self.amount))

class InvenItem():
    """
    Represents an Inventory Item
    :param n: Item name (String)
    :param a: Amount of item you have (Integer)
    """
    def __init__(self, n, a):
        self.name = n
        self.amount = a

    def compare(self, o): ## o: other item to compare
        self.amount += o.amount
        ## Just in case 
        ## if self.name == o.name:
        ##     return True
        ## else:
        ##     return False

    def printInvenItem(self):
        print(self.name + ": " + str(self.amount))

class MainGoal():
    """
    Represents a Main Goal
    :param n: Title of your Goal (String)
    :param d: Description of Goal (String)
    :param i: Items needed for the Goal (InvenItem Array)
    """
    def __init__(self, n, d, i):
        self.name = n
        self.description = d
        self.neededItems = i

    def printMainGoal(self):
        print(self.name + ": " + self.description)

    def canDoGoal(self, i): ## takes in Player inventory, returns a result depending on if the Player's inventory
                            ## has the required Items
                            ## Key:
                            ## Green: You have all the items in the required amount
                            ## Yellow: You have all the required items, but not the required amounts
                            ## Orange: You have at least one of the required items (quantity not withstanding)
                            ## Red: You have none of the required items
                            ## Returns an int from 0 (red) to 3 (green)
        alo = False ## If there's at least one item in your inventory
        for needIt in self.neededItems:
            if needIt.name not in i:
                if alo:
                    return 1
                else:
                    return 0
            elif needIt.amount > i.get(needIt.name).amount:
                return 2
            alo = True
        return 3
        ## TODO: List items you need       

class BonusTask():
    """
    Represents a bonus task assigned on Goal Completion
    :param n: Name of Bonus Task (String)
    :param d: Description of Task (String)
    :param ma: Maximum number of repetitions of the task that needs to be done (Integer)
    :param sa: Set number of repetitions that need to be done (once assigned) (Integer)
    :param ca: Current number of repetitions you still need to do (once assigned) (Integer)
    """
    def __init__(self, n, d, ma, sa = 0, ca = 0):
        self.name = n
        self.desc = d
        self.max_assign = ma
        self.set_assign = sa
        self.cur_assign = ca

    def assignTask(self):
        self.set_assign = random.randint(1, self.max_assign)
        ##print("You will have to do this " + str(self.set_assign) + " times!")

    def incrementTask(self):
        self.cur_assign += 1
        if (self.cur_assign == self.set_assign):
            print("Task Complete!")
            return True
        else:
            return False
        
    def printCurTask(self):
        print(self.name)
        print(self.desc)
        print(str(self.cur_assign) + "/" + str(self.set_assign) + " completed")
