import sys
import string


def count_characters(text: str) -> None:
    """Counts and displays the number of upper-case letters, lower-case

    letters, punctuation marks, spaces, and digits in the given text.
    """
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        elif char in string.punctuation:
            punctuation_count += 1

    total_chars = len(text)

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """Main execution entry point. Parses command-line arguments and

    prompts for user input when needed.
    """
    args = sys.argv[1:]

    try:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")

        if len(args) == 0 or args[0] is None:
            try:
                print("What is the text to count?")
                text = sys.stdin.readline()
            except EOFError:
                text = ""
        else:
            text = args[0]

        count_characters(text)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
