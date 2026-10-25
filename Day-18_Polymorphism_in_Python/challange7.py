class Laptop:
    def show_price(self, price):
        print("Laptop price:", price)

class GamingLaptop(Laptop):
    def show_price(self, price, discount):
        print("Gaming Laptop price:", price)
        print("Discount:", discount)
        final_price = price -((price * discount) / 100)   #amount - ((amount * discount) / 100)
        print("Final Price:", final_price)

class OfficeLaptop(Laptop):
    pass

laptop1 = Laptop()
laptop2 = GamingLaptop()
laptop3 = OfficeLaptop()

all_laptops = [laptop1, laptop2, laptop3]
prices = [50000, [150000,10], 70000]

for item, price in zip(all_laptops, prices):
    if isinstance(item,GamingLaptop):
        laptop_price = price[0]
        discount = price[1]
        item.show_price(laptop_price, discount)
    else:
        item.show_price(price)


# Output:-

"""
Laptop price: 50000
Gaming Laptop price: 150000
Discount: 10
Final Price: 135000.0
Laptop price: 70000
"""