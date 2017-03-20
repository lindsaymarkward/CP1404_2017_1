def main():
    """Demo function scope."""
    x = [3]  # ints are immutable
    print("in main, id is {}".format(id(x)))
    z = function(x)
    print("in main, id is {}".format(id(x)))


def function(y: list) -> None:
    print("in func, id is {}".format(id(y)))
    y += [1]
    print("in func, id is {}".format(id(y)))
    return y

# main()

# print(main.__doc__)
print(function.__annotations__)
