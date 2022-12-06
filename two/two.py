# 1 R
# 2 P
# 3 S

# 0 L
# 3 D
# 6 W
from data import data

# iteration one
wins = {
    "R": "S",
    "P": "R",
    "S": "P"
}

opponent = {
    "A": "R",
    "B": "P",
    "C": "S"
}

player = {
    "X": "R",
    "Y": "P",
    "Z": "S"
}

# iteration two
outcome = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

hand_values = {
    "R": 1,
    "P": 2,
    "S": 3
}

losses = {
    "S": "R",
    "R": "P",
    "P": "S"
}


def part_one():
    total_score = 0

    for x in data:
        game_score = 0
        game = x.split(" ")

        # determine win
        if opponent[game[0]] == player[game[1]]:
            game_score += 3
        elif opponent[game[0]] == wins[player[game[1]]]:
            game_score += 6

        # else lose

        # add points for selection
        if player[game[1]] == "R":
            game_score += 1
        elif player[game[1]] == "P":
            game_score += 2
        else:
            game_score += 3

        total_score += game_score

    print(total_score)


def part_two():
    total_score = 0

    for x in data:
        game_score = 0
        game = x.split(" ")

        # calculate outcome score
        game_score += outcome[game[1]]

        # on draw, add opponent hand value
        if game_score == 3:
            game_score += hand_values[opponent[game[0]]]
        elif game_score == 0:
            game_score += hand_values[wins[opponent[game[0]]]]
        else:
            game_score += hand_values[losses[opponent[game[0]]]]

        total_score += game_score

    print(total_score)


if __name__ == "__main__":
    part_one()
    part_two()
