# import random
# numbers = [10, 20, 30, 40, 50, 100]
# random.shuffle(numbers)
# print(numbers)
# for number in sorted(numbers):
#     print(number, end=' ')

# things = list("things")
# print(things)


def main():
    numbers = [1, 2, 8, 3, 12, 40, 0]
    # print(is_negative_here(numbers))
    print(sorted(numbers))
    # numbers.sort()
    print(numbers)


def is_negative_here(numbers):
    for number in numbers:
        # print("checking...")
        if number < 0:
            return True
    return False


main()
