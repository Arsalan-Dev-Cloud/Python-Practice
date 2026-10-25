class Laptop:

    def __init__(self, obj1):
        self.obj1 = obj1
        
    def show_type(self):
        print("Type:",self.obj1)

class GamingLapotp:

    def __init__(self, obj2):
        self.obj2 = obj2

    def show_type(self):
        print("Type:",self.obj2)


laptop1 = Laptop("Normal Laptop")
laptop2 = GamingLapotp("Gaming Laptop")

laptop1.show_type()
laptop2.show_type()


# Output:-

"""
Type: Normal Laptop
Type: Gaming Laptop
"""