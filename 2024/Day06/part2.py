# Part Two
# https://adventofcode.com/2024/day/6#part2


def move(angle: int, i: int) -> int:
    match angle:
        case 0:  # up
            return i - 131
        case 90:  # right
            return i + 1
        case 180:  # down
            return i + 131
        case 270:  # left
            return i - 1


with open("input.txt", "r") as file:
    text = file.read()

start_position = text.find("^")
guard_position = start_position
guard_angle = 0
visited_positions = set()

# while not off the map
while 0 <= guard_position < len(text) and text[guard_position] != '\n':
    visited_positions.add(guard_position)
    next_position = move(guard_angle, guard_position)

    if text[next_position] == "#":
        guard_angle = (guard_angle + 90) % 360
    else:
        guard_position = next_position

visited_positions.remove(start_position)

# for each unique position the guard visits, test having an obstacle there
potential_obstacle_positions = 0
for obstacle_position in visited_positions:
    guard_position = start_position
    guard_angle = 0
    visited_positions_and_angles = set()

    # Run until loop is found or guard is off the map
    # Idc what you think of while true loops, it made my code less messy and that's more than enough reason to use it
    while True:
        next_position = move(guard_angle, guard_position)

        # Off the map
        if next_position < 0 or next_position > len(text) or text[next_position] == '\n':
            break

        # Found loop
        if (guard_angle, next_position) in visited_positions_and_angles:
            potential_obstacle_positions += 1
            break

        # If the next position is an obstacle, turn right
        if text[next_position] == "#" or next_position == obstacle_position:
            guard_angle = (guard_angle + 90) % 360
        else:
            guard_position = next_position
            visited_positions_and_angles.add((guard_angle, guard_position))

print(potential_obstacle_positions)
