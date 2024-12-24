# Part One
# https://adventofcode.com/2024/day/8

with open("input.txt") as file:
    text = file.read()

antenna_map = text.split("\n")
def valid_coordinates(y, x): return 0 <= y < 50 and 0 <= x < 50

frequency_to_antennas = dict()

# Create a list of antennas for each frequency
for i in range(len(antenna_map)):
    for j in range(len(antenna_map[i])):
        if antenna_map[i][j] == ".":
            continue

        frequency = antenna_map[i][j]
        if frequency in frequency_to_antennas:
            frequency_to_antennas[frequency].append((i, j))
        else:
            frequency_to_antennas[frequency] = [(i, j)]

antinodes = set()

# Find antinodes for each frequency
for frequency in frequency_to_antennas.values():
    for i in range(len(frequency)):
        current_antenna = frequency[i]
        for antenna in frequency[i + 1:]:
            rise = antenna[0] - current_antenna[0]
            run = antenna[1] - current_antenna[1]

            # The one that's twice as far from the current antenna as the other antenna
            far_antinode = (current_antenna[0] + rise * 2, current_antenna[1] + run * 2)

            # The one that's in the direction opposite of the other antenna from the current antenna
            opposite_antinode = (current_antenna[0] + rise * -1, current_antenna[1] + run * -1)

            # Add antinodes if they're valid coordinates
            if valid_coordinates(*far_antinode):
                antinodes.add(far_antinode)
            if valid_coordinates(*opposite_antinode):
                antinodes.add(opposite_antinode)

print(len(antinodes))
