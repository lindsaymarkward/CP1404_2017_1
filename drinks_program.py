"""Program to keep track of appropriate drinking, demonstrating use of classes."""

from drink import Drink
from drinklist import DrinkList

MENU = "Menu: (a)dd a drink, (q)uit"


def main():
    available_drinks = load_drinks("drinks.csv")
    # print([str(drink) for drink in available_drinks])
    my_drinks = DrinkList()
    print(MENU)
    menu_choice = input("> ").lower()
    while menu_choice != 'q':
        if menu_choice == 'a':
            display_available_drinks(available_drinks)
            drink_choice = int(input("? "))
            my_drinks.add(available_drinks[drink_choice])
        else:
            print("Invalid")
        print(my_drinks)
        print(MENU)
        menu_choice = input("> ").lower()
    print(
        "You drank {} drinks ({} were alcoholic for a total of {:.2f} mL alcohol), which cost ${:.2f}".format(
            len(my_drinks), my_drinks.get_number_alcoholic(),
            my_drinks.get_alcohol_volume(), my_drinks.get_total_price()))


def display_available_drinks(drinks):
    for i, drink in enumerate(drinks):
        print("{}. {}".format(i, drink))


def load_drinks(filename):
    all_drinks = []
    input_file = open(filename)
    for line in input_file:
        parts = line.strip().split(',')
        # print(parts)
        all_drinks.append(
            Drink(parts[0], float(parts[1]), float(parts[2]), float(parts[3])))
    input_file.close()
    return all_drinks


main()
