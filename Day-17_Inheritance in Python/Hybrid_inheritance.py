class Laptop:

    def show_brand(self):
        print("Brand: ASUS")


class GamingLaptop(Laptop):

    def show_gpu(self):
        print("GPU: RTX 5050")


class DisplayFeatures:

    def show_refresh_rate(self):
        print("Refresh Rate: 240Hz")


class AdvancedGamingLaptop(GamingLaptop, DisplayFeatures):

    def show_ram(self):
        print("RAM: 16GB DDR5")


laptop = AdvancedGamingLaptop()

laptop.show_brand()
laptop.show_gpu()
laptop.show_refresh_rate()
laptop.show_ram()