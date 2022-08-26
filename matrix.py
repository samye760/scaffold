"""
This program will take a nested list and return the flipped version
"""

from typing import List
import sys


def main(args) -> None:
    """
    Entrypoint of the program
    """

    if not 2 <= len(args) <= 3:
        print("Insuffcient arguments given. Provide one or two.")
        sys.exit()

    if len(args) == 2:
        flip_matrix(args[1])
    else:
        flip_matrix(args[1], args[-1])


def flip_matrix(matrix: List[List[any]], verbose: bool = False) -> List[List[any]]:
    """
    This function takes a list of lists and flips them.
    If the input is invalid, the original input will be returned
    """

    # If the list is empty, return the input
    if not matrix:
        if verbose:
            print("No valid matrix given.")
        return matrix

    # If the input is not a list, return the input
    if not isinstance(matrix, list):
        if verbose:
            print("A list was not given as the argument.")
        return matrix

    if verbose:
        print("\nThe original matrix is the following:\n")
        for inner in matrix:
            print(inner)

    # The dimensions should be equal in order to be flipped
    if len(matrix) != len(matrix[0]):
        if verbose:
            print(
                f"The matrix dimensions ({len(matrix)} x {len(matrix[0])}) are invalid."
            )
        return matrix

    flipped: List[List[any]] = [
        [inner[i] for inner in matrix] for i in range(len(matrix))
    ]

    if verbose:
        print("\nFlipped matrix:\n")
        for inner in flipped:
            print(inner)

    return flipped


if __name__ == "__main__":
    main(sys.argv)
