class Laptop:
    def show_details(self):
        print("Laptop: Basic features")

class GamingLaptop(Laptop):
    def show_details(self):
        super().show_details()
        print("Gaming Laptop: High Performance features")

class OfficeLaptop(Laptop):
    def show_details(self):
        print("Office Laptop: Productivity features")

laptop1 = Laptop()
laptop2 = GamingLaptop()
laptop3 = OfficeLaptop()

all_laptops = [laptop1, laptop2, laptop3]

# Write your for loop here
for item in all_laptops:
    item.show_details()