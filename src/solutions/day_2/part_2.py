import re
import pandas as pd
import numpy as np

with open("src/inputs/day2.txt", "r") as file:
    input = file.readlines()


game_dict = {
    re.search("\d+", re.split(":", value)[0]).group(0): re.split(
        ";", re.split(":", value)[1]
    )
    for value in input
}


def analyze_set(input_set):
    color_list = ["red", "blue", "green"]
    color_regex = "|".join(color_list)

    converted_set = {
        re.search(color_regex, value).group(0): int(re.search("\d+", value).group(0))
        for value in re.split(",", input_set)
    }

    missing_colors = {
        value: 0 for value in list(set(color_list) - set(converted_set.keys()))
    }

    converted_set = {**converted_set, **missing_colors}
    return pd.DataFrame(converted_set, index=[0])


def analyze_game(game):
    df = pd.DataFrame()

    for input_set in game:
        df = pd.concat([df, analyze_set(input_set)], axis=0)

    game_power = np.prod(df.max().to_list())

    return game_power


solution = sum([analyze_game(value) for value in game_dict.values()])

print(solution)
