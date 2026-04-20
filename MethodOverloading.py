class Parent:
    def __init__(self):
        print("in init Parent")

    def show(self):
        print("in show() of Parent class")

class Child(Parent):
    def __init__(self):
        print("in init Child")
    def show(self):
        print("in show() of Child class")

c1 = Child()
c1.show()
