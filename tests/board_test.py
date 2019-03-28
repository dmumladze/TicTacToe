import unittest
from board import Board
from player import Human, Computer

class BoardTest(unittest.TestCase):

    def test(self):
        board = Board()
        board.state = [
            '0',  None, 'X',  
            None, None, 'X', 
            '0',  None, '0'
        ]
        comp = Computer('X')
        comp.play(board)  

        true = board.game_over() and board.winner == 'X'
        self.assertTrue(true)       