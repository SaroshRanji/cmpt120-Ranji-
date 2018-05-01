# simulation.py
from simstats import SimStats
from TennisMatch import TennisMatch

def printIntro():
    print("This program simulates a tennis match")

def getInputs():
    probA = float(input("Enter the probability of A: "))
    probB = float(input("Enter the probability of B: "))
    n = int(input("Number of matches to simulate: "))
    return probA, probB, n
    
def main():
    printIntro()
    probA, probB, n = getInputs()
    stats = SimStats()
    for i in range(n):
        theGame = TennisMatch(probA, probB)
        while not theGame.isMatchOver(probA, probB):
            theGame.play()
            stats.update(theGame)
    stats.printReport()

main()
