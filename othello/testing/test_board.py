import unittest
from othello.game.board import generateBoardValues

class TestBoard(unittest.TestCase):

    def test_matrix(self):
        result = generateBoardValues().get(0).coordinate
        self.assertEqual(result, 'a1')

    def test_change_tile(self):
        board = generateBoardValues()
        result = board.get(0).is_black = True
        self.assertEqual(result, True)
        self.assertEqual(board.get(1).is_black, False)

if __name__ == '__main__':
    unittest.main()