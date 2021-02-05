from num2words import num2words


def is_multiplicable(number, multiplicable):
    """The is_multiplicable function tells if a number is multiplicable by another

       Args:
           number (int): The number to compare.
           multiplicable (int): The multiplicable number to check.

       Returns:
           bool: True if multiplicable, False otherwise.
    """
    return number % multiplicable == 0


def displays_literal_numbers(number, multiplicables_list):
    """The displays_literal_numbers function checks if number multiplicable and returns a literal number if is true

       Args:
           number (int): The number to compare.
           multiplicable (int): The multiplicable numbers list to check.

       Returns:
           str: The string with literal number if number is multiplicable, The int number if is not.
    """
    display = ''

    for multiplicable in multiplicables_list:
        if is_multiplicable(number, multiplicable):
            display += num2words(multiplicable).capitalize()

    if not display:
        display = str(number)

    return display


def detects_multiplicable_numbers(initial_number, final_number, multiplicables):
    for number in range(initial_number, final_number + 1):
        print(number)
