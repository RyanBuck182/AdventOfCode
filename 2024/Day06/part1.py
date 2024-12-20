# Part One
# https://adventofcode.com/2024/day/6


def move(angle: int, i: int) -> int:
    angle %= 360

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

guard_position = text.find("^")
guard_angle = 0
unique_positions = set()

# while not off the map
while 0 <= guard_position < len(text) and text[guard_position] != '\n':
    unique_positions.add(guard_position)
    next_position = move(guard_angle, guard_position)

    if text[next_position] == "#":
        guard_angle += 90
    else:
        guard_position = next_position

print(len(unique_positions))
