from queue import Queue
from math import floor

# Part Two
# https://adventofcode.com/2024/day/5#part2
# This is a very terrible solution.

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


def order_update(update: list[str]) -> list[str]:
    update_set = set(update)
    # Creates subgraph of must_come_after. This subgraph is acyclic.
    update_graph = {page: [curr_page for curr_page in must_come_after[page] if curr_page in update_set]
                    for page in update}

    # Checks if a page is further down the directed graph
    # Breadth-first search
    def comes_after(goal: str, start: str) -> bool:
        frontier = Queue()
        frontier.put(start)

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                return True

            for page in update_graph[current]:
                frontier.put(page)

        return False

    new_update = []
    for old_page in update:
        found = False
        for i in reversed(range(len(new_update))):
            if comes_after(old_page, new_update[i]):
                new_update.insert(i + 1, old_page)
                found = True
                break

        if not found:
            new_update.insert(0, old_page)

    return new_update


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

    if not valid_update:
        ordered_update = order_update(update_pages)
        total += int(ordered_update[floor(len(update_pages) / 2)])

print(total)
