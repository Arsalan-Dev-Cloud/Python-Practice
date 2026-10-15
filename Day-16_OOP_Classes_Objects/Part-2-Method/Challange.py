class Laptop:
    def __init__(self, brand, model, price, discount):
        self.brand = brand
        self.model = model
        self.price = price
        self.discount = discount

    def apply_discount(self):
        # Most common way to calculate discount
        """discount_amount = (self.price * self.discount) / 100
        self.Final_price = self.price - discount_amount"""

        # Another Way to calculate discount (using one line of code & Moderate way)
        self.Final_price = self.price - ((self.price * self.discount) / 100)

        # Programmer Way to calculate discount
        """self.Final_price = self.price
        self.Final_price -= (self.price * self.discount) / 100"""

    def show_details(self):
        print(f"\n{'Brand': <10}: {self.brand}")
        print(f"{'Model': <10}: {self.model}")
        print(f"{'Price': <10}: {self.price}")
        print(f"{'Discount': <10}: {self.discount}")
        print(f"{'Final Price': <10}: {self.Final_price}\n")


laptop1 = Laptop("Asus Rog", "Strix G16", 200000, 20)
laptop2 = Laptop("Dell", "Inspiration 3595", 50000, 10)

laptop1.apply_discount()
laptop2.apply_discount()

laptop1.show_details()
laptop2.show_details()