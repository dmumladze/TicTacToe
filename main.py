from board  import Board
from game   import Game
from player import Human, Computer

board = Board()
game  = Game(board)

game.accept_player(Human('0'))
game.accept_player(Computer('X'))

game.start()            
