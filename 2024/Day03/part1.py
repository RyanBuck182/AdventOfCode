from re import findall

# Part One
# https://adventofcode.com/2024/day/3

with open("input.txt", "r") as file:
    text = file.read()

multiplications = findall(r"mul\((\d+),(\d+)\)", text)

total = 0
for pair in multiplications:
    total += int(pair[0]) * int(pair[1])

print(total)