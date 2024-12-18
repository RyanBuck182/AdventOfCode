from re import findall

# Part Two
# https://adventofcode.com/2024/day/3#part2

file = open("input.txt", "r")
text = file.read()

instructions = findall(r"mul\((\d+),(\d+)\)|(do|don't)\(\)", text)

total = 0
enabled = True
for instruction in instructions:
    if instruction[2] == "do":
        enabled = True
    elif instruction[2] == "don't":
        enabled = False
    elif enabled:  # Multiply
        total += int(instruction[0]) * int(instruction[1])

print(total)