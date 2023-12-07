import re

with open("src/inputs/day1.txt", "r") as file:
    input = file.readlines()

spelled_out_numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def convert_num(number):
    spelled_out_number_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    try:
        converted_number = spelled_out_number_dict[number]
    except KeyError:
        try:
            converted_number = int(number)
        except:
            raise ValueError("Cannot convert to number")
    return converted_number


regex_expression = "|".join(spelled_out_numbers) + "|\d"
reversed_regex = "|".join([val[::-1] for val in spelled_out_numbers]) + "|\d"


def match_string(regex_expression, string):
    match = re.search(regex_expression, string, re.IGNORECASE)
    return string[match.start() : match.end()]


solution = sum(
    [
        10 * convert_num(match_string(regex_expression, string))
        + convert_num(match_string(reversed_regex, string[::-1])[::-1])
        for string in input
    ]
)
print(solution)
