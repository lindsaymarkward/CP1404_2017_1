"""Demo for function scope."""


def main():
    """Demo function scope."""
    x_in_main = [3]  # ints are immutable
    print("in main, id is {}".format(id(x_in_main)))
    # z = function(x)
    print("in main, id is {}".format(id(x_in_main)))


def function(y_parameter: list) -> None:
    """Demonstrate scope."""
    print("in func, id is {}".format(id(y_parameter)))
    y_parameter += [1]
    print("in func, id is {}".format(id(y_parameter)))
    # return y


# on feedback branch
main()
