class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print(f"\n{'Brand': <10}: {self.brand}")
        print(f"{'Model': <10}: {self.model}")
        print(f"{'Price': <10}: {self.price}\n")

mobile1 = Mobile("Poco", "X7 Pro", 25000)
mobile2 = Mobile("Poco", "X8 Pro", 50000)

mobile1.show_details()
mobile2.show_details()