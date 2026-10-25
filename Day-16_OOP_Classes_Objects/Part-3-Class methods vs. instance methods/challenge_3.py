class Laptop:

    @staticmethod
    def check_discount(discount, amount):

        final_price = amount - ((amount * discount) / 100)

        if discount >= 0 and discount <= 100:
            print("Valid Discount")
        else:
            print("Invalid Discount\n")

        print(f"{'Final Price': <15} : ₹{final_price}")

        

#------------------------------------------------------------------------------------------------------------------
print("\n\nEnter -1 to Exit\n\n")

while True:
    
    print("========== Discount Validation ==========\n")
    discount_amount = int(input("Enter Discount: "))

    if discount_amount == -1:
        print("You Got EXIT")
        break
    else:
        Laptop.check_discount(discount_amount, 250000)


# Output :-

"""
Enter -1 to Exit


========== Discount Validation ==========

Enter Discount: 30
Valid Discount
Final Price     : ₹175000.0
========== Discount Validation ==========

Enter Discount: 40
Valid Discount
Final Price     : ₹150000.0
========== Discount Validation ==========

Enter Discount: -1
You Got EXIT
"""