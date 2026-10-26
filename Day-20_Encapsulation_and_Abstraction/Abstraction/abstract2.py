
from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def power_mode(self):
        print("Every laptop has a power mode")


class GamingLaptop(Laptop):

    def power_mode(self):
        super().power_mode()
        print("Gaming Laptop: Performance Mode")


class OfficeLaptop(Laptop):

    def power_mode(self):
        super().power_mode()
        print("Office Laptop: Battery Saver Mode")


laptop1 = GamingLaptop()
laptop2 = OfficeLaptop()

print("--- Gaming Laptop ---")
laptop1.power_mode()

print("\n--- Office Laptop ---")
laptop2.power_mode()


# Output:-

"""
--- Gaming Laptop ---
Every laptop has a power mode
Gaming Laptop: Performance Mode

--- Office Laptop ---
Every laptop has a power mode
Office Laptop: Battery Saver Mode
"""
