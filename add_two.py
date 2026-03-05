#!/usr/bin/env python3
"""Add two numbers provided as command-line arguments."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add two numbers passed as command-line arguments."
    )
    parser.add_argument("number1", type=float, help="The first number")
    parser.add_argument("number2", type=float, help="The second number")
    args = parser.parse_args()

    result = args.number1 + args.number2

    if result.is_integer():
        print(int(result))
    else:
        print(result)


if __name__ == "__main__":
    main()
