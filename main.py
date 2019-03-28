from game   import Game
from player import Human, Computer

game = Game()

game.accept_player(Human())
game.accept_player(Computer())

game.start()            
