class Laptop:

    all_laptops = []

    def __init__(self, brand, model, price, discount, amount):
        self.brand = brand
        self.model = model
        self.price = price
        self.discount = discount
        self.amount = amount
        Laptop.all_laptops.append(self)

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

    def compose_price(self):
        prices = []

        for laptop in Laptop.all_laptops:
            prices.append(laptop.price)

        for i in range(len(prices)):
            larger_count = 0
            for j in range(len(prices)):
                if prices[i] >= prices[j] and i != j:
                    larger_count += 1

            if larger_count == len(prices) - 1:
                self.larger_price = prices[i]


    def show_details(self):
        print(f"\n{'Brand': <10}: {self.brand}")
        print(f"{'Model': <10}: {self.model}")
        print(f"{'Price': <10}: {self.price}")
        print(f"{'Discount': <10}: {self.discount}")
        if hasattr(self, 'Final_price'):
            print(f"{'Final Price': <10}: {self.Final_price}\n")
        print(f"{'Larger Price of Laptop': <10}: {self.larger_price}")


#----------------------------------------------------------------------------------------------------------------------------
laptop1 = Laptop("Asus Rog", "Strix G16", 200000, 20, 50000)
laptop2 = Laptop("Dell", "Inspiration 3595", 50000, 10, 25000)
laptop3 = Laptop("HP", "Pavilion 15", 80000, 15, 30000)

while True:
    num = int(input("Enter 1 to select Apply Discount  &  Enter 2 to select Increase Price : "))
    if num == 1:
        for laptop in Laptop.all_laptops:
            laptop.apply_discount()
        break
    elif num == 2:
        for laptop in Laptop.all_laptops:
            laptop.increase_price()
        break
    else:
        print("Invalid User Input\n")

for laptop in Laptop.all_laptops:
    laptop.compose_price()
    laptop.show_details()