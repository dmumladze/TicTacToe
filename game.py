from board import Board
from player import Player, Human, Computer

class Game:
    def __init__(self, board = Board):
        self.board = board
        self.players = []        

    def accept_player(self, player):
        if len(self.players) == 2:
            raise Exception("Game has sufficient number of players")
        self.players.append(player)

    def start(self):
        self.board.draw(True)
        i = 0         
        while (not self.board.game_over()):  
            try:          
                player = self.players[i]
                if player.is_human():
                    position = int(input(f"\nEnter a position: "))
                    player.play(self.board, position-1)
                else:
                    player.play(self.board)
                i = (i + 1) % 2  
                self.board.draw(True)
            except Exception as e:
                print(str(e))
        
        if self.board.winner == None:
            print("\nDraw")
        else:
            print(f"\nWinner: {self.board.winner}")      