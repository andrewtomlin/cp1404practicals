"""
Program to calculate and display a user's bonus based
on sales. if sales are under $1,000, the user gets a 10% bonus.
Ift sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >=0:
    if sales >= 1000:
        bonus = .15
    else:
        bonus = .1
    print("Your bonus is $", bonus * sales)
    sales = float(input("Enter sales: $"))