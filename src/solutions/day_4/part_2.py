import re
import numpy as np

with open("src/inputs/day4.txt", "r") as file:
    input = file.readlines()

input = [value.strip() for value in input]


def analyze_card_title(card_title):
    return int(re.search("\d+", card_title).group(0))


def analyze_card(card):
    winning_numbers = set(re.findall("\d+", re.split("\|", card)[0]))
    your_numbers = set(re.findall("\d+", re.split("\|", card)[1]))

    win_total = len(your_numbers.intersection(winning_numbers))

    score = win_total

    return score


card_score_dict = {
    analyze_card_title(re.split(":", value)[0]): analyze_card(re.split(":", value)[1])
    for value in input
}

max_card_num = max(card_score_dict.keys())

copy_list = np.array([[0 for i in range(1, max_card_num + 1)]])

for card_num, card_score in card_score_dict.items():
    original = np.array(
        [
            1 if i in range(card_num, card_num + card_score + 1) else 0
            for i in range(1, max_card_num + 1)
        ]
    )

    full = np.array([original * np.sum(copy_list[:, card_num - 1]) + original])

    copy_list = np.append(copy_list, full, axis=0)

solution = sum([copy_list[i, i - 1] for i in range(1, max_card_num + 1)])

print(solution)
