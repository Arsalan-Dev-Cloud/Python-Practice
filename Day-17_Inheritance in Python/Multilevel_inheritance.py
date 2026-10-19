class Laptop:

    def show_brand(self):
        print("Brand: Asus")

class GamingLapotp(Laptop):

    def show_gpu(self):
        print("GPU: RTX 5050")

class AdvanceGamingLaptop(GamingLapotp):

    def show_ram(self):
        print("RAM: 16GB DDR5")


laptop = AdvanceGamingLaptop()

laptop.show_brand()
laptop.show_gpu()
laptop.show_ram()