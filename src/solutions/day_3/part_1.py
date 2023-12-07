import re

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

    character_list = [
        input_array[coordinate[0]][coordinate[1]] for coordinate in coordinate_list
    ]
    part_num_ind = not all([c.isalnum() or c == "." for c in character_list])
    return part_num_ind


solution = sum(
    [
        int(value["part_num"])
        for value in part_num_dict.values()
        if analyze_part_num(**value, input_array=input_array)
    ]
)

print(solution)
