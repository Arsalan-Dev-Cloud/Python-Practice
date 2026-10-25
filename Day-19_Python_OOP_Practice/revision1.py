class Laptop:

    all_obj = []

    def __init__(self, brand):
        self.brand = brand
        Laptop.all_obj.append(self)

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


laptop1 = Laptop("Asus")
laptop2 = GamingLaptop("Acer","RTX 5050")
laptop3 = OfficeLaptop("Dell","16GB")

for item in Laptop.all_obj:
    item.show_details()