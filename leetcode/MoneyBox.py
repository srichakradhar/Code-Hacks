class MoneyBox:
    def __init__(self, capacity):
        """Create a MoneyBox with maximum capacity as capacity"""
        self.box = 0
        self.capacity = capacity
        print("Here is your brand new Money Box that can hold {} coins".format(capacity))

    def can_add(self, v):
        return self.box + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.box += v
            print("Wow! You are richer by {} coins. You have {} coins of capacity left.".format(v, self.capacity - self.box))
        else:
            print("Sorry, your MoneyBox is not big enough. :(")

moneyBox = MoneyBox(10)
moneyBox.add(5)
moneyBox.add(3)
print(moneyBox.box)
moneyBox.add(3)
print(moneyBox.box)

