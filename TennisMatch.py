# TennisMatch.py
from player import Player

class RBallGame:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA
        self.receiving = self.player.B

    def play(self):
        while not self.isOver():
            if self.server.winsServe():
                if self.serving.getScore() == 40 and self.recieving.getScore() < 40:
                    self.serving.incGame()
                    self.serving.resetScore()
                    self.recieving.resetScore()
                elif self.serving.getScore() == 40 and self.recieving.getScore() == 40:
                    if self.recieving.hasAdvantage():
                        self.reveiving.setAdvantage(False)
                    elif self.serving.hasAdvantage():
                        self.serving.incGame()
                        self.serving.resetScore()
                        self.recieving.resetScore()
                    else:
                        self.serving.setAdvantage(True)
                else:
                    self.serving.incScore()

    def getScores(self):
        if self.playerA.getScore() == 60 and self.playerB.getScore() == 60:
            self.playerA.score = 3
            self.playerB.score = 3
        return self.playerA.getScore(), self.playerB.getScore()

    def isOver(self):
        return self.playerA.getScore() == 60 and self.playerB.getScore() < 40 \
            or (self.playerA.getScore() < 40 and self.playerB.getScore() == 60) \
            or (self.playerB.getScore() == 40 and self.playerA.getScore() == 40)

    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA
