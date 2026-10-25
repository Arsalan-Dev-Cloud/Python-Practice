class Laptop:
    
    def show_details(self):
        print("General Laptop")


class GamingLaptop(Laptop):

    def show_details(self):
        print("Gaming Laptop")


class OfficeLapotp(Laptop):

    def show_details(self):
        print("Office Laptop")


laptop1 = Laptop()
laptop2 = GamingLaptop()
laptop3 = OfficeLapotp()

all_laptops = [laptop1, laptop2, laptop3]

for item in all_laptops:
    item.show_details()


# Output:-

"""
General Laptop
Gaming Laptop
Office Laptop
"""