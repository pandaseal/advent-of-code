def get_score(they, result):
    # A = Rock (1), B = Paper (2), C = Scissiors (3)
    # Win (6), lose (0), draw (3)
    # Rock wins over scissors, loses to paper
    # Paper wins over rock, loses to scissors
    # Scissors wins over paper, loses to rock
    score = 0

    if result == "X": # lose
        score += 0
        if they == "A": # rock => scissors
            score += 3
        elif they == "B": # paper => rock
            score += 1
        else: # scissors => paper
            score += 2
    elif result == "Y": # draw
        score += 3
        if they == "A": # rock => rock
            score += 1
        elif they == "B": # paper => paper
            score += 2
        else: # scissors => scissors
            score += 3
    else: # win
        score += 6
        if they == "A": # rock => paper
            score += 2
        elif they == "B": # paper => scissors
            score += 3
        else: # scissors => rock
            score += 1

    return score


def part2():
    sum = 0

    with open('input.txt') as f:
        for line in f:
            game = line.strip().split()
            they = game[0]
            result = game[1]
            sum += get_score(they, result)

    print(sum)

def main():
    part2()

if __name__ == "__main__":
    main()