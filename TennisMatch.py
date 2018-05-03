# rballgame.py
from TennisPlayer import Player

class TennisMatch:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA

    def play(self):
        while not self.isOver():
            if self.server.winsServe():
                self.server.incScore()
            else:
                self.changeServer()

        

    def getScores(self):
        if self.playerA.getScore() == 60 and self.playerB.getScore() == 60:
            self.playerA.score = 3
            self.playerB.score = 3
        return self.playerA.getScore(), self.playerB.getScore()

    def isOver(self):
        return self.playerA.getScore() == 60 and self.playerB.getScore() < 40 \
            or (self.playerA.getScore() < 40 and self.playerB.getScore() == 60)\ \
            or (self.playerB.getScore() == 40 and self.playerA.getScore() == 40)

    def isMatchOver(self, probA, probB):
        while self.playerA.getSetsWon() < 2 and self.playerB.getSetsWon() < 2:
            if self.playerA.getGamesWon() < 6 and self.playerB.getGamesWon() < 6:
                theGame = TennisMatch(probA, probB)
                theGame.play()

    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA
