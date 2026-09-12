# using __init__() method

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

mobile1 = Mobile("Poco", "X7 Pro", 25000)
mobile2 = Mobile("Samsung", "Galaxy S21", 79999)
mobile3 = Mobile("Apple", "iPhone 13", 69999)

print(mobile1.brand, mobile1.model, mobile1.price)
print(mobile2.brand, mobile2.model, mobile2.price) 
print(mobile3.brand, mobile3.model, mobile3.price)

# Output:-
"""
Poco X7 Pro 25000
Samsung Galaxy S21 79999
Apple iPhone 13 69999
"""