from game   import Game
from player import Human, Computer

game = Game()

''' AI against AI
game.accept_player(Computer())
game.accept_player(Computer())
'''

''' Human against AI '''
game.accept_player(Human())
game.accept_player(Computer())

game.start()  
         
