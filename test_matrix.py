from matrix import flip_matrix


def test_matrix() -> None:
    assert flip_matrix([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert flip_matrix([[]]) == [[]]
    assert flip_matrix("hi") == "hi"
