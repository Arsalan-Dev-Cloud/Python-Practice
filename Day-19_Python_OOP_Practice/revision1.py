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


class OfficeLaptop(Laptop):

    def __init__(self, brand, ram):
        super().__init__(brand)
        self.ram = ram

    def show_details(self):
        super().show_details()
        print("Ram:",self.ram)




laptop1 = OfficeLaptop("Dell","16GB")
laptop1.show_details()