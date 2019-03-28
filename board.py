import os
import math
from collections import namedtuple
from copy import deepcopy

class Board():
    win_states = [            
        [0, 1, 2],#horizontal
        [3, 4, 5],   
        [6, 7, 8],            
        [0, 3, 6],#vertical
        [1, 4, 7],
        [2, 5, 8],            
        [0, 4, 8],#crossing
        [2, 4, 6]
    ]    
    def __init__(self):
        self.state = [
            None, None, None,  
            None, None, None, 
            None, None, None
        ]
        self.__winner = None
        self.__empty = len(self.state)
        self.__position = 0
    
    def is_legal(self, position):        
        return self.state[position] == None

    def apply(self, mark, position):
        if not self.is_legal(position):
            raise Exception(f"Illegal move for '{mark}' at position {position}")
        self.state[position] = mark
        self.__empty -= 1
        self.__position = position

    def game_over(self):     
        for wstate in Board.win_states: 
            wi0 = wstate[0]
            wi1 = wstate[1]
            wi2 = wstate[2]
            if self.state[wi0] != None and self.state[wi0] == self.state[wi1] and self.state[wi1] == self.state[wi2]:
                self.__winner = self.state[wi0]
                return True                   
        return self.__empty == 0

    def get_children(self, mark):
        children = []
        for i, v in enumerate(self.state):
            if v == None:
                child = deepcopy(self)                      
                child.apply(mark, i)
                children.append(child)
        return children

    def get_position(self):
        return self.__position        
    position = property(get_position)         
                    
    def get_winner(self):
        return self.__winner        
    winner = property(get_winner) 

    def get_state(self):
        return self.__state     
    def set_state(self, value):
        self.__state = value  
        self.__empty = sum(x == None for x in value) 
    state = property(get_state, set_state)               

    def draw(self, clear = bool):
        if clear == True:
            os.system("cls")      
        print(" %s | %s | %s " % (self.state[0] or "1",self.state[1] or "2",self.state[2] or "3"))    
        print("___|___|___")    
        print(" %s | %s | %s " % (self.state[3] or "4",self.state[4] or "5",self.state[5] or "6"))    
        print("___|___|___")    
        print(" %s | %s | %s " % (self.state[6] or "7",self.state[7] or "8",self.state[8] or "9"))    
        
