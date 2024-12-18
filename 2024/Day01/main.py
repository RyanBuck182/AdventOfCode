file = open("input.txt", "r")

# Part One

lefts = []
rights = []
for line in file:
    space = line.find(" ")
    lefts.append(int(line[:space]))
    rights.append(int(line[space:]))

lefts.sort()
rights.sort()

total = 0
for i in range(len(lefts)):
    total += abs(lefts[i] - rights[i])

print(total)

# Part Two

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