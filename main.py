from menu import MenuItem#, Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine


espresso = MenuItem(name="Espresso", cost=3, milk=200, water=100, coffee=25)
latte = MenuItem(name="Latte", cost=3, milk=200, water=100, coffee=25)
cappuccino = MenuItem(name="Cappuccino", cost=3, milk=200, water=100, coffee=25)
# espresso.ingredients = {"water": 100, "coffee": 25}


print(espresso.name)
for n in espresso.ingredients:
    print(f"{n} = {espresso.ingredients[n]}")

