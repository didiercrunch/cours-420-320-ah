from tdd.fizzbuzz import fizz_buzz


def test_fizz_buzz():
    assert len(fizz_buzz()) == 100


def test_fizz_buzz_1():
    assert fizz_buzz()[0] == 1


def test_fizz_buzz_2():
    assert fizz_buzz()[2] == "Fizz"
