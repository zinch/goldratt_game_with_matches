from matches_game import Boy
import matches_game
import unittest.mock as mock

def test_records_number_of_matches():
    boy = Boy("Andy")
    with mock.patch('matches_game.cast_die', lambda: 4):
        boy.make_move()
    with mock.patch('matches_game.cast_die', lambda: 6):
        boy.make_move()

    assert boy.moves == [4, 6]

def test_records_score_for_each_move():
    boy = Boy("Randy")
    boy.stock = 3 + 5
    with mock.patch('matches_game.cast_die', lambda: 3):
        boy.make_move()

    with mock.patch('matches_game.cast_die', lambda: 5):
        boy.make_move()

    assert boy.scores == [-0.5, 1.5]
    assert boy.total_score() == 1

def test_records_number_of_matches():
    boy = Boy("Andy")
    boy.stock = 1
    next_boy = Boy("Sam")
    boy.set_next(next_boy)
    with mock.patch('matches_game.cast_die', lambda: 4):
        boy.make_move()

    assert boy.stock == 0
    assert boy.scores == [-2.5]
    assert next_boy.stock == 1

    with mock.patch('matches_game.cast_die', lambda: 3):
        next_boy.make_move()

    assert next_boy.stock == 0

    return
    with mock.patch('matches_game.cast_die', lambda: 1):
        boy.make_move()
    with mock.patch('matches_game.cast_die', lambda: 6):
        next_boy.make_move()

    assert next_boy.moves == [3, 1]

