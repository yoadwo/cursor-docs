import argparse


def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply_numbers(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Perform simple math operations on two numbers."
    )
    subparsers = parser.add_subparsers(dest="command", help="Operation to perform")

    # Sum subcommand
    sum_parser = subparsers.add_parser("sum", help="Add two numbers")
    sum_parser.add_argument("a", type=float, help="First number")
    sum_parser.add_argument("b", type=float, help="Second number")

    # Multiply subcommand
    multiply_parser = subparsers.add_parser("multiply", help="Multiply two numbers")
    multiply_parser.add_argument("a", type=float, help="First number")
    multiply_parser.add_argument("b", type=float, help="Second number")

    args = parser.parse_args()

    if args.command == "sum":
        result = add_numbers(args.a, args.b)
    elif args.command == "multiply":
        result = multiply_numbers(args.a, args.b)
    else:
        parser.print_help()
        return

    print(result)


if __name__ == "__main__":
    main()