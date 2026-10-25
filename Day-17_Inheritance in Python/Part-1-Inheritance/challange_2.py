# Program for single inheritance

class Laptop:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Price: ₹{self.price}")


class BusinessLaptop(Laptop):

    def show_purpose(self):
        print("Purpose: Business and productivity")



laptop1 = BusinessLaptop("ASUS ROG Strix G16", 200000)

laptop1.show_details()
laptop1.show_purpose()


# Output:-

"""
Brand: ASUS ROG Strix G16
Price: ₹200000
Purpose: Business and productivity
"""