"""
Write a program that asks the user for their age and then
prints whether it is odd or even.
The program should not crash if the user enters a non-number
The program should not allow an invalid age number
Re-prompt until a valid number is entered
"""


def main():
    age = 0
    valid_input = False
    while not valid_input:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be >= 0")
            else:
                valid_input = True
        except ValueError:
            print("Invalid input. Enter a number")

    if is_even(age):
        print("{} is even".format(age))
    else:
        print("{} is odd".format(age))


def is_even(number):
    return number % 2 == 0

    # if number % 2 == 0:
    #     return True
    # else:
    #     return False


def test_is_even():
    for i in range(5):
        print("{} is {}".format(i, is_even(i)))


main()
# test_is_even()
