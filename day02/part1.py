def calc_score(they, you):
    # A, X # Rock (1)
    # B, Y # Paper (2)
    # C, Z # Scissiors (3)
    # Win (6), lose (0), draw (3)
    # Rock wins over scissors, loses to paper
    # Paper wins over rock, loses to scissors
    # Scissors wins over paper, loses to rock
    score = 0

    if you == "X": # rock
        score += 1
        if they == "A": # rock => draw
            score += 3
        elif they == "B": # paper => loss
            score += 0
        else: # scissors => win
            score += 6
    elif you == "Y": # paper
        score += 2
        if they == "A": # rock => win
            score += 6
        elif they == "B": # paper => draw
            score += 3
        else: # scissors => loss
            score += 0
    else: # scissors
        score += 3
        if they == "A": # rock => loss
            score += 0
        elif they == "B": # paper => win
            score += 6
        else: # scissors => draw
            score += 3

    return score

sum = 0

with open('input.txt') as f:
    for line in f:
        game = line.strip().split()
        they = game[0]
        you = game[1]
        sum += calc_score(they, you)

print(sum)
