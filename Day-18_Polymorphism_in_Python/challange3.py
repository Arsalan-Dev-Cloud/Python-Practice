class Laptop:

    def show_details(self):
        print("Laptop: Basic features")

class GamingLaptop:

    def show_details(self):
        print("Gaming Laptop: High Performance features")


laptop1 = Laptop()
laptop2 = GamingLaptop()

laptop1.show_details()
laptop2.show_details()