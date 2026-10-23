class Laptop:
    def show_price(self, price):
        print("Laptop price:", price)

class GamingLaptop(Laptop):
    def show_price(self, price):
        print("Gaming Laptop price:", price)

class OfficeLaptop(Laptop):
    pass

laptop1 = Laptop()
laptop2 = GamingLaptop()
laptop3 = OfficeLaptop()

all_laptops = [laptop1, laptop2, laptop3]
prices = [50000, 150000, 70000]

for item, price in zip(all_laptops, prices):
    item.show_price(price)