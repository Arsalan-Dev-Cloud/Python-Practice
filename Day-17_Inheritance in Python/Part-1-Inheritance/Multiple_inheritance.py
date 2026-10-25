class Laptop:

    def show_brand(self):
        print("Brand: Asus")

class Gaming_Features:

    def show_gpu(self):
        print("GPU: RTX 5050")

class GamingLaptop(Laptop, Gaming_Features):

    def show_refesh_rate(self):
        print("Refresh Rate: 240Hz")


laptop1 = GamingLaptop()

laptop1.show_brand()
laptop1.show_gpu()
laptop1.show_refesh_rate()


# Output-

"""
Brand: Asus
GPU: RTX 5050
Refresh Rate: 240Hz
"""