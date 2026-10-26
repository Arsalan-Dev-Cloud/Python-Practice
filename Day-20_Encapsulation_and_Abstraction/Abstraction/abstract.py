from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def start(self):
        pass


class GamingLaptop(Laptop):

    def start(self):
        print("Gaming laptop starting...")


class OfficeLaptop(Laptop):

    def start(self):
        print("Office laptop starting...")


laptop1 = GamingLaptop()
laptop2 = OfficeLaptop()

laptop1.start()
laptop2.start()