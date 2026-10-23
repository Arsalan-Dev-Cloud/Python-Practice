all_laptops = []


class Laptop:
    def show_details(self):
        print("General Laptop")


class GamingLaptop(Laptop):
    def show_details(self):
        print("Gaming Laptop")


class OfficeLaptop(Laptop):
    def show_details(self):
        print("Office Laptop")


def create_laptop(laptop_type):
    laptop = laptop_type()
    all_laptops.append(laptop)
    return laptop


# Create and register objects
laptop1 = create_laptop(Laptop)
laptop2 = create_laptop(GamingLaptop)
laptop3 = create_laptop(OfficeLaptop)

# Display all registered laptops
for item in all_laptops:
    item.show_details()
