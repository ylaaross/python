import sys

# Mandatory dictionary mapping supported characters to Morse Code strings
NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def encode_to_morse(text: str) -> str:
    """Encodes an alphanumeric string into Morse code using NESTED_MORSE.

    Raises an AssertionError if an unsupported character is encountered.
    """
    morse_output = []

    for char in text.upper():
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse_output.append(NESTED_MORSE[char])

    # Join all converted characters and strip any trailing space
    return "".join(morse_output).strip()


def main():
    """Main execution point.

    Parses command-line arguments, validates input, and prints the encoded
    Morse string.
    """
    args = sys.argv[1:]

    try:
        if len(args) != 1:
            raise AssertionError("the arguments are bad")

        result = encode_to_morse(args[0])
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
