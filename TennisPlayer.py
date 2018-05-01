# player.py
from random import *

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0
        self.GamesWon = 0
        self.SetsWon = 0

    def winsServe(self):
        # Returns true with probability self.prob
        return random() <= self.prob

    def incScore(self):
        # Add a point to this player's score
        self.score = self.score + 1

    def getScore(self):
        if self.score == 1:
            return 15
        elif self.score == 2:
            return 30
        elif self.score == 3:
            return 40
        elif self.score == 4:
            return 60
        else:
            return self.score
        # Return this player's current score
      
    def getGamesWon(self):
        return self.GamesWon

    def getSetsWon(self):
        return self.SetsWon
