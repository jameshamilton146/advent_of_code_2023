import re
import itertools

with open("src/inputs/day5.txt", "r") as file:
    input = file.readlines()

start_field = "seed"
end_field = "location"
input = [value.strip() for value in input]

seed_vals = [int(value) for value in re.findall("\d+", re.split(":", input[0])[1])]
maps_input = input[2:]


def split_list(lst, val):
    return [
        list(group) for k, group in itertools.groupby(lst, lambda x: x == val) if not k
    ]


maps_input = split_list(maps_input, "")

maps_dict = {re.sub(" map:$", "", value[0]): value[1:] for value in maps_input}


def split_map_code(map_code):
    map_values = [int(value) for value in re.split(" ", map_code)]
    return map_values


def create_mapper_function(map_values):
    def map_num(num):
        if num not in range(map_values[1], map_values[1] + map_values[2]):
            raise ValueError("input outside of function range")
        mapped_num = num - map_values[1] + map_values[0]

        return mapped_num

    return map_num


def construct_mapping_dict(map_list):
    def return_self(num):
        return num

    mapping_dict = {
        **{
            i: {
                "input_range": [
                    split_map_code(v)[1],
                    split_map_code(v)[1] + split_map_code(v)[2],
                ],
                "mapping_function": create_mapper_function(split_map_code(v)),
            }
            for i, v in enumerate(map_list)
        },
        **{
            len(map_list): {
                "input_range": [float("-inf"), float("inf")],
                "mapping_function": return_self,
            }
        },
    }

    return mapping_dict


def map_val(val, mapping_dict):
    for value in mapping_dict.values():
        if val >= value["input_range"][0] and val <= value["input_range"][1]:
            mapped_val = value["mapping_function"](val)

            break
        else:
            next
    return mapped_val


def full_map_val(val, mapping_dict_list):
    mapped_val = val
    for mapping_dict in mapping_dict_list:
        mapped_val = map_val(mapped_val, mapping_dict)

    return mapped_val


def find_map_link_order(start_field, end_field, map_titles):
    map_links = [re.split("-to-", value) for value in map_titles]

    seq = []

    for i in range(0, len(map_links)):
        map_link = [value for value in map_links if value[0] == start_field][0]

        seq.append(f"{map_link[0]}-to-{map_link[1]}")

        start_field = map_link[1]

        if start_field == end_field:
            break

    return seq


map_link_order = find_map_link_order(
    start_field=start_field, end_field=end_field, map_titles=maps_dict.keys()
)

mapping_dict_list = [
    construct_mapping_dict(maps_dict[map_link]) for map_link in map_link_order
]

solution = min([full_map_val(seed_val, mapping_dict_list) for seed_val in seed_vals])

print(solution)
