# Use of __init__() method in python
class Mobile:
    def __init__(self):
        print("Mobile Object Created")

mobile1 = Mobile()
mobile2 = Mobile()
mobile3 = Mobile()

# Output:- 
"""
Mobile Object Created
Mobile Object Created
Mobile Object Created
"""

# Use of __init__() method in python with attributes
class Mobile:
    def __init__(self):
        self.brand = "Poco"

mobile1 = Mobile()
print(mobile1.brand)

# Output:- Poco
