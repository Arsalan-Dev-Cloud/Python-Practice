# This is the program to understand inheritance
class Laptop:

    def __init__(self, brand, price, G_card):
        self.brand = brand
        self.price = price
        self.G_card = G_card


    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Price: ₹{self.price}")


class GamingLaptop(Laptop):
    
    def show_gpu(self):
        print(f"GPU: {self.G_card}")


laptop1 = GamingLaptop("Strix G16", 200000, "RTX 5050")

laptop1.show_details()
laptop1.show_gpu()