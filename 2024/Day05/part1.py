from math import floor

# Part One
# https://adventofcode.com/2024/day/5

with open("input.txt", "r") as file:
    text = file.read()

rules, updates = text.split("\n\n")

# Stores the pages that must be printed before the given page
must_come_after = {}

# Populates must_come_after
for rule in rules.split("\n"):
    page_a, page_b = rule.split("|")
    if page_a in must_come_after:
        must_come_after[page_a].append(page_b)
    else:
        must_come_after[page_a] = [page_b]

# Checks update validity and calculates middle totals
total = 0
for update in updates.split("\n"):
    valid_update = True
    update_pages = update.split(',')
    processed_pages = set()

    for current_page in update_pages:
        # If a page had been processed even though it was supposed to come after the current page, invalidate the update
        if any(page in processed_pages for page in must_come_after[current_page]):
            valid_update = False
            break
        else:
            processed_pages.add(current_page)

    if valid_update:
        total += int(update_pages[floor(len(update_pages) / 2)])

print(total)
