"""A small example application for the GitHub Actions linting demo."""


def greet(name):
    """Return a friendly greeting for a name."""
    return f"Hello, {name}!"


def add_numbers(first, second):
    """Return the sum of two numbers."""
    return first + second


def main():
    """Run the example program."""
    message = greet("GitHub Actions")
    total = add_numbers(2, 3)

    print(message)
    print(f"2 + 3 = {total}")


if __name__ == "__main__":
    main()
