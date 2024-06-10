from num2words import num2words


def is_multiplicable(number: int, multiplicable: int) -> bool:
    """The is_multiplicable function tells if a number is multiplicable by another

       Args:
           number (int): The number to compare.
           multiplicable (int): The multiplicable number to check.

       Returns:
           bool: True if multiplicable, False otherwise.
    """
    return number % multiplicable == 0


def detects_multiplicable_numbers(number_to_check: int, multiplicables: list[int]) -> str:
    """The detects_multiplicable_numbers function checks if number multiplicable and returns a literal number if is true

       Args:
           number_to_check (int): The number to compare.
           multiplicables (list[int]): The multiplicable numbers list to check.

       Returns:
           str: The string with literal number if number is multiplicable, The int number if is not.
    """
    display = ''

    for multiplicable in multiplicables:
        if is_multiplicable(number_to_check, multiplicable):
            display += num2words(multiplicable).capitalize()

    if not display:
        display = str(number_to_check)

    return display


def displays_detected_numbers(first_number: int, last_number: int, multiplicables: list[int]) -> list[str]:
    """The displays_detected_numbers function iterates the numbers to lines

       Args:
           first_number (int): The initial number to start the iteration.
           last_number (int): The final number to start the iteration.
           multiplicables (list[int]): The multiplicable numbers list to check.

       Returns:
           list: The list of strings with literal number if number is multiplicable, The int number if is not.
    """

    lines_to_display = []

    for number in range(first_number, last_number + 1):
        verified_number = detects_multiplicable_numbers(number, multiplicables)
        lines_to_display.append(verified_number)

    return lines_to_display


def main():
    import argparse

    parser = argparse.ArgumentParser(description='A command line tools that tells if is multiple numbers.')
    parser.add_argument('-m', '--multiplicables', type=int, nargs='*', default=[3, 5],
                        help='The multiplicable numbers to do the detections.')
    parser.add_argument('-i', '--first-number', type=int, default=1,
                        help='The initial number to start the iteration')
    parser.add_argument('-f', '--last-number', type=int, default=100,
                        help='The final number to start the iteration')
    args = parser.parse_args()

    # executes the detections and build a list of lines
    lines_to_display = displays_detected_numbers(args.first_number, args.last_number, args.multiplicables)

    # converts list to string output
    output_string = '\n'.join(lines_to_display)

    # show on user screen
    print(output_string)


if __name__ == '__main__':
    main()
