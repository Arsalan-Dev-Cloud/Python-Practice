class Laptop:

    def __init__(self, brand):
        self.brand = brand

    def show_details(self):
        print("Brand:",self.brand)


class GamingLaptop(Laptop):

    def __init__(self, brand, gpu):
        super().__init__(brand)
        self.gpu = gpu

    def show_details(self):
        super().show_details()
        print("GPU:",self.gpu)

laptop1 = GamingLaptop("Asus","RTX 5050")
laptop1.show_details()