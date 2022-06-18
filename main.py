# imports
import math

# Global variables
price = input("Enter the price of the item: ")
discount_1 = input("Enter first discount: ")  # float(price) / 100 * 3.5
# float(price) / 100 * 5
discount_2 = input("Enter second discount (If there is any): ")
discount_3 = input("Enter third discount (If there is any): ")
discount_4 = input("Enter fourth discount (If there is any): ")

# calculate vat
vat = float(price) / 100 * 20
nonvat = float(price) - vat

# discounts
discount = float(discount_1) + float(discount_2) + \
    float(discount_3) + float(discount_4)
after = float(price) - float(discount)

# print the results
print("The price of the item without vat is: ", nonvat)
print("The price of the item with vat is: ", vat)
print("The price of the item after discounts is: ", after)
