class Laptop:

    def show_details(self):
        print("Laptop: Basic features")

class GamingLaptop(Laptop):

    def show_details(self):
        super().show_details()
        print("Gaming Laptop: High Performance features")

laptop1 = GamingLaptop()
laptop1.show_details()