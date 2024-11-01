import unittest
from unittest.mock import patch
from rock_paper_scissors import check_winner, get_computer_play

class TestRockPaperScissors(unittest.TestCase):
    
    def test_check_winner_tie(self):
        self.assertEqual(check_winner("rock", "rock"), "The game is a tie.")
        self.assertEqual(check_winner("paper", "paper"), "The game is a tie.")
        self.assertEqual(check_winner("scissors", "scissors"), "The game is a tie.")

    def test_check_winner_user_wins(self):
        self.assertEqual(check_winner("rock", "scissors"), "You win!")
        self.assertEqual(check_winner("paper", "rock"), "You win!")
        self.assertEqual(check_winner("scissors", "paper"), "You win!")

    def test_check_winner_computer_wins(self):
        self.assertEqual(check_winner("scissors", "rock"), "The computer wins!")
        self.assertEqual(check_winner("rock", "paper"), "The computer wins!")
        self.assertEqual(check_winner("paper", "scissors"), "The computer wins!")

    @patch('random.randint')
    def test_get_computer_play(self, mock_randint):
        mock_randint.return_value = 0
        self.assertEqual(get_computer_play(), "rock")
        
        mock_randint.return_value = 1
        self.assertEqual(get_computer_play(), "paper")
        
        mock_randint.return_value = 2
        self.assertEqual(get_computer_play(), "scissors")

if __name__ == "__main__":
    unittest.main()