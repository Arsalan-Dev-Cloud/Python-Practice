class Laptop:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:",self.brand)

class GamingLaptop(Laptop):

    def __init__(self, brand, type, GPU):
        super().__init__(brand)
        self.type = type
        self.gpu = GPU

    def show_type(self):
        print("Type:",self.type)

    def show_gpu(self):
        print("GPU:",self.gpu)

class BusinessLapotp(Laptop):

    def __init__(self, brand, purpose):
        super().__init__(brand)
        self.purpose = purpose

    def show_type(self):
        print("Type: Business Laptop")

    def show_purpose(self):
        print("Purpose:",self.purpose)

laptop1 = GamingLaptop("ASUS","Gaming Lapotp","RTX 5050")
laptop2 = BusinessLapotp("Dell","Professional use")

laptop1.show_brand()
laptop1.show_type()
laptop1.show_gpu()

print()

laptop2.show_brand()
laptop2.show_type()
laptop2.show_purpose()



# Ouput:-

"""
Brand: ASUS
Type: Gaming Lapotp
GPU: RTX 5050

Brand: Dell
Type: Business Laptop
Purpose: Professional use
"""