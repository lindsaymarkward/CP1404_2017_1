"""CP1404 in-class demos for recursion."""


def main():
    print_down_loop(4)
    print_down(4)
    # numbers = [1, 2, 3]
    # print(sum_list_iteratively(numbers))
    # print(sum_list(numbers))


def recurse(n):
    if n <= 0:
        print("Thing!")
    else:
        print(n)
        recurse(n - 1)
        print(n)


def print_down_loop(start):
    n = start
    while n >= 0:
        print(n)
        n -= 1


def print_down(n):
    print(n)
    if n > 0:
        print_down(n - 1)


def sum_list_iteratively(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def sum_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + sum_list(numbers[1:])
