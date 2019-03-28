from collections import namedtuple
from board import Board

class Player:
    def __init__(self):
        self.mark = None
        self.opponent = None     

    def play(self, state = Board, position = None):
        pass 

    def is_human(self):
        return False

class Human(Player):
    def is_human(self):
        return True

    def play(self, board = Board, position = None):
        board.apply(self.mark, position) 

class Computer(Player):
    def play(self, board = Board):   
        analysis = namedtuple("Analysis", ["depth", "nodes"])  
        analysis.depth = 0
        analysis.nodes = 0
        (state, _) = self.maximize(board, float('-Inf'), float('Inf'), analysis)
        board.apply(self.mark, state.position)  

    def maximize(self, state, alpha, beta, analysis, depth = 0):
        if state.game_over():
            return (None, self.evaluate(state))

        (maxChild, maxUtility) = (None, float('-Inf'))
        
        children = state.get_children(self.mark)        
        if depth > analysis.depth:
            analysis.depth = depth
        analysis.nodes += len(children)

        for child in children:       
            (_, utility) = self.minimize(child, alpha, beta, analysis, depth+1)
            if utility > maxUtility:
                (maxChild, maxUtility) = (child, utility)            
            
            if maxUtility >= beta:
                break
            if maxUtility > alpha:
                alpha = maxUtility
                        
        return (maxChild, maxUtility)

    def minimize(self, state, alpha, beta, analysis, depth = 0):
        if state.game_over(): 
            return (None, self.evaluate(state))
        
        (minChild, minUtility) = (None, float('Inf'))

        children = state.get_children(self.opponent)
        if depth > analysis.depth:
            analysis.depth = depth
        analysis.nodes += len(children)

        for child in children: 
            (_, utility) = self.maximize(child, alpha, beta, analysis, depth+1)  
            if utility < minUtility:
                (minChild, minUtility) = (child, utility)
            
            if minUtility <= alpha:
                break        
            if minUtility < beta:
                beta = minUtility             
            
        return (minChild, minUtility)
    
    def evaluate(self, state):
        if state.winner == self.mark:
            return 10
        elif state.winner == self.opponent:
            return -10
        else:
            return 0                
