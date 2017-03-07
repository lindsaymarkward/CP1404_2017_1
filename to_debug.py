
def is_valid_label(label):
    """
    Determine if the input label matches the requirements:
    labels must start with a capital, have at least 5 characters
    and at least one number
    :return: True if label is valid, otherwise False
    """
    if len(label) < 5:
        return False
    if not label[0].isupper():
        return False
    for char in label:
        if not char.isnumeric():
            return False
    return True

