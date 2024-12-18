# Part Two
# https://adventofcode.com/2024/day/2#part2

# Check if two integers are increasing relative to each other
def increasing(level_a: int, level_b: int) -> bool:
    return level_b - level_a > 0


# Check if the report is increasing
def is_report_increasing(levels: list[int]) -> bool:
    increase_1 = increasing(levels[0], levels[1])
    increase_2 = increasing(levels[1], levels[2])
    increase_3 = increasing(levels[2], levels[3])

    return ((increase_1 and increase_2)
            or (increase_1 and increase_3)
            or (increase_2 and increase_3))


# Get the difference between two levels
def get_difference(level_a: int, level_b: int) -> int:
    return abs(level_a - level_b)


# Check if the difference between two levels is acceptable
def acceptable_difference(level_a: int, level_b: int) -> bool:
    return 1 <= get_difference(level_a, level_b) <= 3


# Check if the report is safe
def is_report_safe(levels: list[int], level_was_removed: bool = False) -> bool:
    report_is_increasing = is_report_increasing(levels)
    report_is_safe = True

    # Ensure consistent increase or decrease
    def consistent_change(level_a: int, level_b: int) -> bool:
        return report_is_increasing == increasing(level_a, level_b)

    # Check each level pair for safety
    i = 0
    while i != len(levels) - 1:
        if not (consistent_change(levels[i], levels[i + 1])
                and acceptable_difference(levels[i], levels[i + 1])):
            if level_was_removed:
                report_is_safe = False
                break
            else:
                # Remove each of the problem levels to see if it becomes safe
                copy1 = levels.copy()
                copy1.pop(i)
                copy2 = levels.copy()
                copy2.pop(i + 1)
                return is_report_safe(copy1, True) or is_report_safe(copy2, True)
        i += 1

    return report_is_safe


file = open("input.txt", "r")
safe_report_count = 0

for line in file:
    if is_report_safe([int(x) for x in line.split()]):
        safe_report_count += 1

print(safe_report_count)
