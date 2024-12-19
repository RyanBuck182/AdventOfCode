from re import findall, DOTALL

# Part Two
# https://adventofcode.com/2024/day/4#part2

with open("input.txt", "r") as file:
    text = file.read()


def match_count(regex: str) -> int:
    regex = "(?=" + regex + ")"
    return len(findall(regex, text, DOTALL))


total = 0
total += match_count(r"M.M.{139}A.{139}S.S")  # M's Up
total += match_count(r"S.S.{139}A.{139}M.M")  # M's Down
total += match_count(r"M.S.{139}A.{139}M.S")  # M's Left
total += match_count(r"S.M.{139}A.{139}S.M")  # M's Right

print(total)
