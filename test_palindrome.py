from palindrome import is_palindrome


def test_is_palindrome() -> None:

    assert is_palindrome("racecar") is True
    assert is_palindrome("not a palindrome") is False
    assert is_palindrome("adfadfkkdf") is False
    assert is_palindrome("redrum sir is murder") is True
    assert is_palindrome("35reDR%#U   M    sI  R #$# is ()*muR*(  der") is True
