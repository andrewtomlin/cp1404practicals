total = 0
Number_of_items = int(input("Enter number of items"))
for i in range(0, Number_of_items, 1):
    value_of_item = int(input("Price of item :"))
    total += value_of_item
if total > 100:
    discount = total * 0.1
    total = total - discount
print("Total price for", Number_of_items, "items is ${:.2f}".format(total))
