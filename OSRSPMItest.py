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

test = ChanceItem("Baby Impling Jar", 0, 1000, ["Basically", "Nothing"], ["Everything Else"])
print("Doot")
test.printChanceItem()