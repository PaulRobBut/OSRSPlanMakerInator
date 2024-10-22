## Classes
class ChanceItem():
    """
    Represents a Chance Item
    :param n: Item name (String)
    :param a: Amount of said item you have (Integer)
    :param p: Price of Chance Item (in GP) (Integer)
    :param g: Good Items in drop table (String Array)
    :param b: Junk items in drop table (String Array)
    :param pm: Does accessing the drop table require a PK risk? (Boolean)
    :param i: Additional item needed to access drop table (String)
    """
    def __init__(self, n = "Commorb", a = 0, p = 1, g = [], b = [], pk = False, i = "None"):
        self.name = n
        self.amount = a
        self.price = p
        self.good_items = g
        self.bad_items = b
        self.pkRisk = pk
        self.itemNeeded = i

    def printChanceItem(self):
        print(self.name)
        print(self.amount)
        print(self.price)
        print(self.good_items)
        print(self.bad_items)
        print(self.pkRisk)
        print(self.itemNeeded)

    ## TODO: Realign print, aligning sections to columns via tabbing
    def displayChanceItem(self):
        print(self.name + ", (" + str(self.price) + " GP ea, Needed Item: " + self.itemNeeded + ", PK Risk: " + str(self.pkRisk) + "): " + str(self.amount))

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
