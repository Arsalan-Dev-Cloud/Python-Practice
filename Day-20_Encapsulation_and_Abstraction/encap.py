class Laptop:

    def __init__(self, battery):
        self.__battery = battery

    def show_battery(self):
        print("Battery:", self.__battery)

    def set_battery(self, battery):

        if battery >= 0 and battery <= 100:
            self.__battery = battery
        else:
            print("Invalid battery percentage!")


laptop1 = Laptop(70)

laptop1.show_battery()

laptop1.set_battery(90)
laptop1.show_battery()

laptop1.set_battery(-20)
laptop1.show_battery()