import re

with open("src/inputs/day1.txt", "r") as file:
    test = file.readlines()

solution = sum(
    [
        int(re.findall(r"\d", string)[0] + re.findall(r"\d", string)[-1])
        for string in test
    ]
)

print(solution)
