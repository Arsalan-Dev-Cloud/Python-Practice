
class Laptop:
    all_laptops = []

    def __init__(self):
        Laptop.all_laptops.append(self)

    def show_details(self):
        print("General Laptop")


class GamingLaptop(Laptop):
    def show_details(self):
        print("Gaming Laptop")


class OfficeLaptop(Laptop):
    def show_details(self):
        print("Office Laptop")


# Create objects
laptop1 = Laptop()
laptop2 = GamingLaptop()
laptop3 = OfficeLaptop()

# Display all registered laptops
for item in Laptop.all_laptops:
    item.show_details()
