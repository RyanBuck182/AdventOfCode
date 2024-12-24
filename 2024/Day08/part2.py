# Part Two
# https://adventofcode.com/2024/day/8#part2

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

            # Coordinates in the direction of the current antenna (up)
            current_coord = current_antenna
            while valid_coordinates(*current_coord):
                antinodes.add(current_coord)
                current_coord = (current_coord[0] - rise, current_coord[1] - run)

            # Coordinates in the direction of the antenna (down)
            current_coord = antenna
            while valid_coordinates(*current_coord):
                antinodes.add(current_coord)
                current_coord = (current_coord[0] + rise, current_coord[1] + run)

print(len(antinodes))
