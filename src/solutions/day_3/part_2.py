import re
import numpy as np

with open("src/inputs/day3.txt", "r") as file:
    input = file.readlines()
input = [value.strip() for value in input]

part_num_dict = {}
j = 0
for i, line in enumerate(input):
    for match in re.finditer("\d+", line):
        part_num_dict[j] = {
            "part_num": match.group(0),
            "row_num": i,
            "start": match.start(),
            "end": match.end() - 1,
        }
        j += 1

input_array = [list(value) for value in input]

asterisk_coordinates = []
for i, value in enumerate(input_array):
    for j, item in enumerate(value):
        if item == "*":
            asterisk_coordinates.append((i, j))


def analyze_part_num(row_num, start, end, input_array, **kwargs):
    max_col_index = len(input_array[0]) - 1
    max_row_index = len(input_array) - 1
    coordinate_list = []

    if row_num - 1 >= 0:
        for value in [*range(max(start - 1, 0), min(end + 1, max_col_index) + 1)]:
            coordinate_list.append((row_num - 1, value))
    if start - 1 >= 0:
        coordinate_list.append((row_num, start - 1))
    if end + 1 <= max_col_index:
        coordinate_list.append((row_num, end + 1))
    if row_num + 1 <= max_row_index:
        for value in [*range(max(start - 1, 0), min(end + 1, max_col_index) + 1)]:
            coordinate_list.append((row_num + 1, value))

    return coordinate_list


part_num_coordinate_dict = {
    key: {
        "part_num": value["part_num"],
        "coordinates": analyze_part_num(**value, input_array=input_array),
    }
    for key, value in part_num_dict.items()
}


def analyze_asterisk(asterisk_coord, part_num_coordinate_dict):
    matching_part_nums = [
        int(value["part_num"])
        for value in part_num_coordinate_dict.values()
        if asterisk_coord in value["coordinates"]
    ]

    return matching_part_nums


gear_connects = [
    analyze_asterisk(
        asterisk_coord=asterisk_coord, part_num_coordinate_dict=part_num_coordinate_dict
    )
    for asterisk_coord in asterisk_coordinates
]


def analyze_gear_connect(gear_connect):
    if len(gear_connect) == 2:
        gear_ratio = np.prod(gear_connect)
    else:
        gear_ratio = 0

    return gear_ratio


solution = sum([analyze_gear_connect(gear_connect) for gear_connect in gear_connects])

print(solution)
