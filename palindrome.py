"""
This program takes command line arguments to test if
a phrase is a palindrome or not
"""
from sys import argv


def is_palindrome(phrase: str, verbose: bool = False) -> bool:
    """
    Takes a phrase (string) and returns True if the lowercase alpha
    characters result in a palindrome and False if not
    """
    left, right = 0, len(phrase) - 1

    while left < right:
        if not phrase[left].isalpha():
            left += 1
            continue

        if not phrase[right].isalpha():
            right -= 1
            continue

        if phrase[left].lower() != phrase[right].lower():
            if verbose:
                print(
                    f"Original phrase stripped of non alpha chars: "
                    f"{''.join([char.lower() for char in phrase if char.isalpha()])} \
                    \nReversed stripped phrase: "
                    f"{''.join([char.lower() for char in phrase if char.isalpha()])[::-1]}"
                )

            return False

        left += 1
        right -= 1

    if verbose:
        print(
            f"{''.join([char.lower() for char in phrase if char.isalpha()])} "
            "is a valid palindrome of "
            f"{''.join([char.lower() for char in phrase if char.isalpha()][::-1])}"
        )

    return True


def main(args=None) -> None:
    """
    Entrypoint of program
    """

    if len(args) == 3:
        is_palindrome(argv[1], argv[2])
    else:
        try:
            is_palindrome(argv[1])
        except IndexError as err:
            print(err, end="")
            print(" - this program takes one required argument and one optional")


if __name__ == "__main__":
    main(argv)
