class Laptop:

    all_obj = []

    def __init__(self, brand):

        self.brand = brand
        Laptop.all_obj.append(self)

    def show_details(self):
        print("Brand:", self.brand)


class GamingLaptop(Laptop):

    def __init__(self, brand, gpu):
        super().__init__(brand)
        self.gpu = gpu

    def show_details(self):
        super().show_details()
        print("GPU:", self.gpu)


class OfficeLaptop(Laptop):

    def __init__(self, brand, RAM):
        super().__init__(brand)
        self.ram = RAM        

    def show_details(self):
        super().show_details()
        print("RAM:",self.ram)


laptop1 = Laptop("Asus")
laptop2 = GamingLaptop("Acer", "RTX 5050")
laptop3 = OfficeLaptop("Dell", "16GB")
laptop4 = GamingLaptop("MSI", "RTX 5070")

for item in Laptop.all_obj:
    item.show_details()


# Output:-

"""
Brand: Asus
Brand: Acer
GPU: RTX 5050
Brand: Dell
RAM: 16GB
Brand: MSI
GPU: RTX 5070
"""