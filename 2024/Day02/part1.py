# Part One
# https://adventofcode.com/2024/day/2

# Check if two integers are increasing relative to each other
def increasing(level_a: int, level_b: int) -> bool:
    return level_b - level_a > 0


# Get the difference between two levels
def get_difference(level_a: int, level_b: int) -> int:
    return abs(level_a - level_b)


# Check if the difference between two levels is acceptable
def acceptable_difference(level_a: int, level_b: int) -> bool:
    return 1 <= get_difference(level_a, level_b) <= 3


file = open("input.txt", "r")
safe_report_count = 0

for line in file:
    levels = [int(x) for x in line.split()]
    report_is_increasing = increasing(levels[0], levels[1])
    report_is_safe = True

    # Ensure consistent increase or decrease
    def consistent_change(level_a: int, level_b: int) -> bool:
        return report_is_increasing == increasing(level_a, level_b)

    for i in range(len(levels) - 1):
        if not (consistent_change(levels[i], levels[i + 1])
                and acceptable_difference(levels[i], levels[i + 1])):
            report_is_safe = False
            break

    if report_is_safe:
        safe_report_count += 1

print(safe_report_count)
