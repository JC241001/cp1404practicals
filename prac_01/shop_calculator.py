"""
The program allows the user to enter the number of items and the
price of each different item. Then the program computes and displays the total
price of those items. If the total price is over $100, then
a 10% discount is applied to that total before the amount is displayed on the screen.
"""


num_items = int(input("Please Enter the number of items: "))
total_price = 0
valid_input = False

while not valid_input:
    if num_items < 0:
        print("Invalid number of items!")
        num_items = int(input("Please Enter the number of items: "))
    else:
        valid_input = True

for i in range(num_items):
    total_price = total_price + float(input("Price of items: "))

# Apply 10% discount if total price is more than $100
if total_price > 100:
    total_price = total_price - total_price * 0.1

print("Total price for {} items is ${:.2f}".format(num_items, total_price))