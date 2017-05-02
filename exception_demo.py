"""Demo of non-local exception catching."""


def main():
    # local catching version
    print("Hello")
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age... using 0")
        age = 0
    print("You are {} years old".format(age))


# main()


def non_local():
    # non-local catching version
    print("Hello")
    try:
        age = get_age()
    except ValueError:
        # the exception generated inside the function is caught here
        print("Invalid age... using 0")
        age = 0
    print("You are {} years old".format(age))


def get_age():
    # the exception is generated here and not handled
    # it is passed out of the function
    return int(input("Age: "))


non_local()
