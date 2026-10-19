class Laptop:

    def show_brand(self):
        print("Brand: Asus")

class GamingLaptop(Laptop):

    def show_gpu(self):
        print("GPU: RTX 5050")

class AdvancedGamingLaptop(Laptop):

    def show_ram(self):
        print("RAM: 16GB DDR5")

laptopx = AdvancedGamingLaptop()
laptopy = GamingLaptop()

laptopx.show_brand()
laptopy.show_brand()

laptopx.show_ram()
laptopy.show_gpu()