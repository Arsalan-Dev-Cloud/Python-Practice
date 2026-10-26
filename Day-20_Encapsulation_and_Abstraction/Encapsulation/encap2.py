class Laptop:

    def __init__(self, battery):
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        if 0 <= value <= 100:
            self.__battery = value
        else:
            print("Invalid battery percentage!")


laptop1 = Laptop(70)

print(laptop1.battery)

laptop1.battery = 90
print(laptop1.battery)

laptop1.battery = -20
print(laptop1.battery)

laptop1.battery = 110
print(laptop1.battery)
