class Laptop:

    all_laptops = []

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        Laptop.all_laptops.append(self)

    def show_details(self):
        print(f"\n{'Brand': <10}: {self.brand}")
        print(f"{'Model': <10}: {self.model}")
        print(f"{'Price': <10}: {self.price}\n")

    @classmethod
    def laptop_count(cls):
        print("\n========== Laptop Statistics ==========\n")
        print(f"{'Total Laptops': <10}: {len(cls.all_laptops)}\n")
    

#----------------------------------------------------------------------------------------------------------------------------

laptop1 = Laptop("Asus Rog", "Strix G16", 200000)
laptop2 = Laptop("Dell", "Inspiration 3595", 50000)
laptop3 = Laptop("HP", "Pavilion 15", 80000)


print("\n========== Laptop Details ==========\n")
for laptop in Laptop.all_laptops:
    laptop.show_details()

Laptop.laptop_count()