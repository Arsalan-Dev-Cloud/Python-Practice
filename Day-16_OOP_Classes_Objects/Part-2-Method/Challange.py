class Laptop:
    def __init__(self, brand, model, price, discount, amount):
        self.brand = brand
        self.model = model
        self.price = price
        self.discount = discount
        self.amount = amount

    def apply_discount(self):
        # Most common way to calculate discount
        """discount_amount = (self.price * self.discount) / 100
        self.Final_price = self.price - discount_amount"""

        # Another Way to calculate discount (using one line of code & Moderate way)
        self.Final_price = self.price - ((self.price * self.discount) / 100)

        # Programmer Way to calculate discount
        """self.Final_price = self.price
        self.Final_price -= (self.price * self.discount) / 100"""

    def increase_price(self):
        self.price += self.amount

    def show_details(self):
        print(f"\n{'Brand': <10}: {self.brand}")
        print(f"{'Model': <10}: {self.model}")
        print(f"{'Price': <10}: {self.price}")
        print(f"{'Discount': <10}: {self.discount}")
        if hasattr(self, 'Final_price'):
            print(f"{'Final Price': <10}: {self.Final_price}\n")


laptop1 = Laptop("Asus Rog", "Strix G16", 200000, 20, 50000)
laptop2 = Laptop("Dell", "Inspiration 3595", 50000, 10, 25000)

while True:
    num = int(input("Enter 1 to select Apply Discount  &  Enter 2 to select Increase Price : "))
    if num == 1:
        laptop1.apply_discount()
        laptop2.apply_discount()
        break
    elif num == 2:
        laptop1.increase_price()
        laptop2.increase_price()
        break
    else:
        print("Invalid User Input\n")


laptop1.show_details()
laptop2.show_details()