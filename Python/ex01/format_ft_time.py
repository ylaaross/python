import time
from datetime import datetime


def main():
    """Formats and prints the current date and time in specific formats."""
    current_time = time.time()
    formatted_seconds = f"{current_time:,.4f}"
    scientific_seconds = f"{current_time:.2e}"

    print(
        f"Seconds since January 1, 1970: {formatted_seconds} "
        f"or {scientific_seconds} in scientific notation"
    )

    now = datetime.now()
    formatted_date = now.strftime("%b %d %Y")
    print(formatted_date)


if __name__ == "__main__":
    main()
