# using __init__() method

class Mobile:
    def __init__(self, brand):
        self.brand = brand

mobile1 = Mobile("Poco")
mobile2 = Mobile("Samsung")
mobile3 = Mobile("Apple")

print(mobile1.brand)
print(mobile2.brand)
print(mobile3.brand)

# Output:-
"""
Poco
Samsung
Apple
"""