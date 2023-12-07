import re

with open("src/inputs/day2.txt", "r") as file:
    input = file.readlines()


game_dict = {
    re.search("\d+", re.split(":", value)[0]).group(0): re.split(
        ";", re.split(":", value)[1]
    )
    for value in input
}


def analyze_set(set):
    color_regex = "blue|red|green"

    max_map = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    actual = {
        re.search(color_regex, value).group(0): int(re.search("\d+", value).group(0))
        for value in re.split(",", set)
    }

    return all([value <= max_map[key] for key, value in actual.items()])


def analyze_game(game):
    return all([analyze_set(set) for set in game])


solution = sum(
    [int(key) for key, value in game_dict.items() if analyze_game(value) == True]
)

print(solution)
