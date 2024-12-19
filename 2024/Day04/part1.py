from re import findall, DOTALL

# Part One
# https://adventofcode.com/2024/day/4

with open("input.txt", "r") as file:
    text = file.read()


def match_count(regex: str) -> int:
    regex = "(?=" + regex + ")"
    return len(findall(regex, text, DOTALL))


total = 0
total += match_count(r"XMAS")  # Forward
total += match_count(r"SAMX")  # Backward
total += match_count(r"X.{140}M.{140}A.{140}S")  # Vertical
total += match_count(r"S.{140}A.{140}M.{140}X")  # Upside-down Vertical
total += match_count(r"X.{141}M.{141}A.{141}S")  # Down-right diagonal
total += match_count(r"X.{139}M.{139}A.{139}S")  # Down-left diagonal
total += match_count(r"S.{139}A.{139}M.{139}X")  # Up-right diagonal
total += match_count(r"S.{141}A.{141}M.{141}X")  # Up-left diagonal

print(total)