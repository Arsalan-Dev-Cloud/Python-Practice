class Laptop:

    def show_details(self):
        print("Laptop: Basic features")

class GamingLaptop:

    def show_details(self):
        print("Gaming Laptop: High Performance features")

class OfficeLaptop:

    def show_details(self):
        print("Office Laptop: Productivity features")

class Smartphone:

    def show_details(self):
        print("Smartphone: Mobile features")


laptop1 = Laptop()
laptop2 = GamingLaptop()
laptop3 = OfficeLaptop()
mobile1 = Smartphone()


allobj = [laptop1,laptop2,laptop3, mobile1]

for item in allobj:
    item.show_details()


# Output:-

"""
Laptop: Basic features
Gaming Laptop: High Performance features
Office Laptop: Productivity features
Smartphone: Mobile features
"""
