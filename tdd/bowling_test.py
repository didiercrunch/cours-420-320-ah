from tdd.bowling import BowlingGame


def test_new_game():
    bowling_game = BowlingGame()


def test_new_game_trivial():
    bowling_game = BowlingGame()
    bowling_game.throw(5)
    assert bowling_game.score() == 5


def test_new_game_trivial_2():
    bowling_game = BowlingGame()
    bowling_game.throw(5)
    bowling_game.throw(3)
    assert bowling_game.score() == 8


def test_new_game_trivial_3():
    bowling_game = BowlingGame()
    bowling_game.throw(6)
    bowling_game.throw(4)

    bowling_game.throw(3)
    assert bowling_game.score() == 16
