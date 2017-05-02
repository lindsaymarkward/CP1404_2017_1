"""
Write a function to take in a filename and return the longest line
of the file: (line number, length)
"""


def get_longest_line(filename):
    """ open filename for reading as file
        line_number, length = ??
        close file
        return (line_number, length) as tuple
    """
    # input_file = open(filename, 'r')
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()
        lengths = [len(line.strip()) for line in lines]
        max_length = max(lengths)
        which_line = lengths.index(max_length)
    # input_file.close()
    return which_line + 1, max_length


# print(".gitignore, expect: (1, 6)")
print(get_longest_line(".gitignore"))
