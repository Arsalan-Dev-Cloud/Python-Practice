
class Laptop:

    def __init__(self, battery):
        self.__battery = battery

    def show_battery(self):
        print("Battery:", self.__battery)
        print("Current battery:", self.get_battery(), "%")

    def set_battery(self, battery):
        if battery >= 0 and battery <= 100:
            self.__battery = battery
        else:
            print("Invalid battery percentage!")

    def get_battery(self):
        return self.__battery


laptop1 = Laptop(70)

laptop1.show_battery()

laptop1.set_battery(90)
laptop1.show_battery()

laptop1.set_battery(-20)
laptop1.show_battery()


# Output:-

"""
Battery: 70
Current battery: 70 %
Battery: 90
Current battery: 90 %
Invalid battery percentage!
Battery: 90
Current battery: 90 %
"""
