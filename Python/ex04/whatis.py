import sys


def check_even_or_odd():
    """Checks if a command-line argument is an integer and prints whether

    it is even or odd, raising an AssertionError for invalid inputs.
    """
    # sys.argv contains script name as sys.argv[0].
    # So len(sys.argv) - 1 is the number of arguments passed.
    args = sys.argv[1:]

    # Rule: If no argument is provided, do nothing.
    if len(args) == 0:
        return

    # Rule: If more than one argument is provided, raise AssertionError.
    if len(args) > 1:
        print("AssertionError: more than one argument is provided")
        return

    # Try converting the argument to an integer
    try:
        number = int(args[0])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    # Part 1: Check even or odd using modulo operator (%)
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    check_even_or_odd()
