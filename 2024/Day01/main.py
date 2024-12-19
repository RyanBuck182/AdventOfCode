# Part One
# https://adventofcode.com/2024/day/1

file = open("input.txt", "r")

lefts, rights = [], []
for line in file:
    space = line.find(" ")
    lefts.append(int(line[:space]))
    rights.append(int(line[space:]))
file.close()

lefts.sort()
rights.sort()

total = 0
for i in range(len(lefts)):
    total += abs(lefts[i] - rights[i])

print(total)

# Part Two
# https://adventofcode.com/2024/day/1#part2

occurrences = {}
for num in rights:
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1

similarity = 0
for num in lefts:
    similarity += num * occurrences[num] if num in occurrences else 0

print(similarity)