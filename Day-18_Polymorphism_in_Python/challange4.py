class Laptop:

    def show_details(self):
        print("Laptop: Basic features")

class GamingLaptop(Laptop):

    def show_details(self):
        print("Gaming Laptop: High Performance features")

class officeLaptop(Laptop):
    pass

laptop1 = Laptop()
laptop2 = GamingLaptop()
laptop3 = officeLaptop()

laptop1.show_details()
laptop2.show_details()
laptop3.show_details()