import io, typing
from pathlib import Path


def is_balanced_file_object(file_object: typing.IO[str]) -> bool:
    text = file_object.read()
    counter = 0
    for letter in text:
        if letter == "(":
            counter += 1
        if letter == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


def is_balanced_file(file_path: Path) -> bool:
    with open(file_path, "r") as file_:
        return is_balanced_file_object(file_)


def test_is_balanced_file_object() -> None:
    assert is_balanced_file_object(io.StringIO(""))
    assert is_balanced_file_object(io.StringIO("()"))
    assert is_balanced_file_object(io.StringIO("(()())"))
    assert not is_balanced_file_object(io.StringIO("((())"))
    assert not is_balanced_file_object(io.StringIO("(()))"))
    assert not is_balanced_file_object(io.StringIO(")"))


def get_first_two_numbers(lst, target):
    for e in lst:
        if (target - e) in lst:
            return tuple(sorted((e, target - e)))


def test_get_two_numbers():
    lst = [55, 20, 76, 34, 80, 26]
    target = 100
    assert get_first_two_numbers(lst, target) == (20, 80)


def test_get_two_numbers_2():
    lst = [55, 80, 76, 34, 20, 26]
    target = 100
    assert get_first_two_numbers(lst, target) == (20, 80)


def test_get_two_numbers_3():
    lst = [55, 30, 80, 76, 34, 70, 20, 26]
    target = 100
    # assert get_first_two_numbers(lst, target) == (20, 80)
