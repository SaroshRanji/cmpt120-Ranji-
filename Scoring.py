#scoring.py
scoreA = 0
scoreB = 0
while not(scoreA == 15 or scoreB == 15 or \
          (scoreA == 7 and scoreB ==0) or \
          (scoreA == 0 and scoreB == 7)):
    print("Playing...")
    scoreA = scoreA + 1
    #continue playing
