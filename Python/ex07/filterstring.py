import sys


def filter_words(text: str, length: int) -> list[str]:
    """Filters words from text whose length is strictly greater than length

    using a lambda function and a list comprehension.
    """
    is_longer = lambda w: len(w) > length
    return [word for word in text.split() if is_longer(word)]


def main():
    """Main execution entry point.

    Validates command-line arguments and outputs the filtered list of words.
    """
    args = sys.argv[1:]

    try:
        if len(args) != 2:
            raise AssertionError("the arguments are bad")

        # Ensure the first argument is not a pure integer string
        try:
            int(args[0])
            raise AssertionError("the arguments are bad")
        except ValueError:
            pass

        # Validate that the second argument is a valid integer
        try:
            length_threshold = int(args[1])
        except ValueError:
            raise AssertionError("the arguments are bad")

        result = filter_words(args[0], length_threshold)
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()