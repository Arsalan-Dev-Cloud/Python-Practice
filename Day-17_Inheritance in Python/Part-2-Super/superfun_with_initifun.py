class Laptop:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

class GamingLaptop(Laptop):

    def __init__(self, brand, gpu, ram):
        super().__init__(brand)
        self.gpu = gpu
        self.ram = ram

    def show_details(self):
        self.show_brand()
        print("GPU:",self.gpu)
        print("RAM:",self.ram)

laptop1 = GamingLaptop("ASUS","RTX 5050","16GB DDR5")
laptop1.show_details()