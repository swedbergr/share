import pytest
from rock_paper_scissors import check_winner, get_computer_play
from unittest.mock import patch

def test_check_winner_tie():
    assert check_winner("rock", "rock") == "The game is a tie."
    assert check_winner("paper", "paper") == "The game is a tie."
    assert check_winner("scissors", "scissors") == "The game is a tie."

def test_check_winner_user_wins():
    assert check_winner("rock", "scissors") == "You win!"
    assert check_winner("paper", "rock") == "You win!"
    assert check_winner("scissors", "paper") == "You win!"

def test_check_winner_computer_wins():
    assert check_winner("scissors", "rock") == "The computer wins!"
    assert check_winner("rock", "paper") == "The computer wins!"
    assert check_winner("paper", "scissors") == "The computer wins!"

@pytest.mark.parametrize("mock_return, expected_play", [
    (0, "rock"),
    (1, "paper"),
    (2, "scissors")
])
@patch('random.randint')
def test_get_computer_play(mock_randint, mock_return, expected_play):
    mock_randint.return_value = mock_return
    assert get_computer_play() == expected_play