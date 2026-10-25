class Laptop:

    def show_type(self):
        print("General-purpose lapotop")

class Gaminglaptop(Laptop):

    def show_type(self):
        print("Gaming laptop - RTX 5050")

class BusinessLaptop(Laptop):

    def show_type(self):
        print("Business laptop - Professional use")


laptop1 = Laptop()
laptop2 = Gaminglaptop()
laptop3 = BusinessLaptop()

laptop1.show_type()
laptop2.show_type()
laptop3.show_type()


# Output:-

"""
General-purpose lapotop
Gaming laptop - RTX 5050
Business laptop - Professional use
"""