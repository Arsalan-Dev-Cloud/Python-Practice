class Laptop:

    def show_brand(self):
        print("Brand: ASUS")

class GamingLaptop(Laptop):

    def show_details(self):
        super().show_brand()
        print("GPU: RTX 5050")

laptop1 = GamingLaptop()

laptop1.show_details()