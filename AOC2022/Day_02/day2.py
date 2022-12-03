# Opponent          # Me
# A = Rock          # # X = Rock
# B = Paper         # # Y = Paper
# C = Scissors      # # Z = Scissors
# A > C > B > A
# Total Score = sum(all scoreseach round)
# If I played the round by selecting Rock, score for shape is 1
# If I played the round by selecting Paper, score for shape is 2
# If I played the round by selecting Scissors score for shape is 3
# If I won the round  + 6, draw + 3, lost 0 point I get

data = open('input.txt', 'r')
totalScore = 0
roundScore = 0
for i in data.readlines():
    if i[0] == 'A': # Rock
        if i[2] == 'X': # Lose
            totalScore += 3 + 1
            roundScore += 0 + 3
        elif i[2] == 'Y': # draw
            totalScore += 6 + 2
            roundScore += 3 + 1
        elif i[2] == 'Z': # win
            totalScore += 0 + 3
            roundScore += 6 + 2
    elif i[0] == 'B': # Paper
        if i[2] == 'X': # lose
            totalScore += 0 + 1
            roundScore += 0 + 1
        elif i[2] == 'Y': # draw
            totalScore += 3 + 2
            roundScore += 3 + 2
        elif i[2] == 'Z': # win
            totalScore += 6 + 3
            roundScore += 6 + 3
    elif i[0] == 'C': # Scissors
        if i[2] == 'X': # lose
            totalScore += 6 + 1
            roundScore += 0 + 2
        elif i[2] == 'Y': # draw
            totalScore += 0 + 2
            roundScore += 3 + 3
        elif i[2] == 'Z': # win
            totalScore += 3 + 3
            roundScore += 6 + 1
print(totalScore)
print(roundScore)
