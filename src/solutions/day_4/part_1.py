import re

with open("src/inputs/day4.txt", "r") as file:
    input = file.readlines()

input = [value.strip() for value in input]


def analyze_card(card):
    winning_numbers = set(re.findall("\d+", re.split("\|", card)[0]))
    your_numbers = set(re.findall("\d+", re.split("\|", card)[1]))

    win_total = len(your_numbers.intersection(winning_numbers))

    score = 2 ** (win_total - 1) if win_total > 0 else 0

    return score


solution = sum([analyze_card(re.split(":", value)[1]) for value in input])

print(solution)
