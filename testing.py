import doctest


def is_adult(age):
    """
    >>> is_adult(12)
    False
    >>> is_adult(99)
    True
    >>> is_adult(18)
    True
    """
    return age >= 18


# print(is_adult(19))

# assert not is_adult(17)
# assert is_adult(18), "Not working"
# assert is_adult(19)


def is_odd(n):
    return n % 2

assert is_odd(1)
assert not is_odd(10)

doctest.testmod()
