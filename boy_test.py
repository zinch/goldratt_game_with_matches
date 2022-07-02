from matches_game import Boy
import matches_game
import unittest.mock as mock

def test_records_number_of_matches():
    boy = Boy("Andy")
    with mock.patch('matches_game.cast_die', lambda: 4):
        assert matches_game.cast_die() == 4
        boy.make_move()
    with mock.patch('matches_game.cast_die', lambda: 6):
        boy.make_move()

    assert boy.moves == [4, 6]

def test_records_score_for_each_move():
    boy = Boy("Randy")
    with mock.patch('matches_game.cast_die', lambda: 3):
        boy.make_move()

    with mock.patch('matches_game.cast_die', lambda: 5):
        boy.make_move()

    assert boy.scores == [-0.5, 1.5]
