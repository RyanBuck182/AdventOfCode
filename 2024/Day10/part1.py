from re import finditer
from queue import Queue

# Part One
# https://adventofcode.com/2024/day/10

with open("input.txt") as file:
    topographic_map = file.read()


# Returns the cardinal neighbors of a position on the map
def get_cardinal_neighbors(position: int) -> list[int]:
    return [
        position - 56,  # up
        position + 1,  # right
        position + 56,  # down
        position - 1  # left
    ]


# Checks if a coordinate is within the bounds of the map
def in_bounds(position: int) -> bool:
    return position % 56 != 55 and 0 <= position < len(topographic_map)


# Returns the cardinal neighbors of a position on the map that are within bounds
def get_valid_cardinal_neighbors(position: int) -> list[int]:
    return [neighbor for neighbor in get_cardinal_neighbors(position) if in_bounds(neighbor)]


# Breadth-first search finding all summits that can be reached by a valid trail starting from the trailhead
def get_trailhead_score(trailhead: int) -> int:
    summits = set()
    frontier = Queue()

    frontier.put(trailhead)

    current = None
    while not frontier.empty():
        current = frontier.get()
        current_height = int(topographic_map[current])

        if current_height == 9:
            summits.add(current)

        neighbors = get_valid_cardinal_neighbors(current)
        for neighbor in neighbors:
            neighbor_height = int(topographic_map[neighbor])
            if neighbor_height - current_height == 1:
                frontier.put(neighbor)

    return len(summits)


total = 0
trailheads = map(int, [match.start() for match in finditer(r"0", topographic_map)])
for head in trailheads:
    total += get_trailhead_score(head)

print(total)
