# From Day 16 onwards, you will be creating your own PyCharm projects from scratch.
# Instead of using templates that I have created for you.
# It will be another step in your journey as a developer!
# But don't worry, I will explain how to do everything in the video tutorials on Udemy.


# import another_module
#
# print(another_module.another_variable)
# from turtle import Turtle, Screen


# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red4", "pink")
# timmy.forward(100)
# timmy.right(90)
#
# timmy.backward(120)
# timmy.left(90)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

