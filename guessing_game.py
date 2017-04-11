
"""
Ask the user to guess a number between 1 and 10 and keep asking
until they get it right.
Use a constant for the secret number
Just use "? " as the prompt for now"""

# PROMPT = '?: '
# SECRET_NUMBER = 0
#
# #  keep going until...
# number = int(input(PROMPT))
# while number != SECRET_NUMBER:
#     print("guess again")
#     number = int(input(PROMPT))
# print("You got it!")

# s = "Hello world"
# for i in range(len(s)):
#     print(i)
#
# for char in s:
#     print(char)

# for i, char in enumerate(s):
#     print("At index {:2} is {:8}".format(i, char))


def main():
    """ Guessing game main """
    in_file = open("age_test.py", 'r')
    # text = in_file.readline()
    in_file.readline()
    line = ""
    for line in in_file:
        line = line.strip('\n')
        print(repr(line))

    out_file = open("test.txt", "w")
    try:
        print(line, file=out_file)
    except NameError:
        pass
    in_file.close()
    out_file.close()


main()
