import unittest
from othello.game.board import generateBoardValues

class TestBoard(unittest.TestCase):

    def test_matrix(self):
        result = generateBoardValues().get('0').coordinate
        self.assertEqual(result, 'a1')

if __name__ == '__main__':
    unittest.main()