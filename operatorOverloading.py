class House:
    def __init__(self,price):
        self.price = price

    def __gt__(self, other):
        if (self.price > other.price):
            return True
        else:
            return False

if __name__ == "__main__":
    h1 = House(900)
    h2 = House(999)

    print(h1.price)
    print(h2.price)

    if h1 > h2:
        print("House1 has higher price")
    else:
        print("House2 has higher price")