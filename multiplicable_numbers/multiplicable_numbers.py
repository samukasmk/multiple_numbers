def is_multiplicable(number, multiplicable):
    """The is_multiplicable function tells if a number is multiplicable by another

       Args:
           number (int): The number to compare.
           multiplicable (int): The multiplicable number to check.

       Returns:
           bool: The return value. True if multiplicable, False otherwise.
    """
    return number % multiplicable == 0


def detects_multiplicable_numbers(initial_number, final_number, multiplicables):
    for number in range(initial_number, final_number + 1):
        print(number)
