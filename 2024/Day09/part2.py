# Part Two
# https://adventofcode.com/2024/day/9#part2

with open("input.txt") as file:
    disk_map = file.read()

filesystem = []

# Creates the file system from the disk map
is_file = True
for i in range(len(disk_map)):
    if is_file:
        file_id = int(i / 2)
        file_size = int(disk_map[i])
        filesystem += [(file_id, file_size)]
    else:
        space_size = int(disk_map[i])
        if space_size != 0:
            filesystem += [(-1, space_size)]

    is_file = not is_file

# Compresses the file system
i = len(filesystem)
while i >= 0:
    i -= 1

    # Skip free spaces
    if filesystem[i][0] == -1:
        continue

    file_size = filesystem[i][1]
    free_space_index = None

    # Search the filesystem for a free space that can fit the current file
    for j in range(i):
        is_free_space = filesystem[j][0] == -1
        is_enough_space = filesystem[j][1] >= file_size

        if is_free_space and is_enough_space:
            free_space_index = j
            break

    # No adequate free space was found for the given file
    if free_space_index is None:
        continue

    is_just_enough_space = filesystem[free_space_index][1] == file_size

    if is_just_enough_space:
        filesystem[free_space_index] = filesystem[i]
    else:  # Free space is larger than the file
        remaining_space = filesystem[free_space_index][1] - file_size
        filesystem[free_space_index] = (-1, remaining_space)
        filesystem.insert(free_space_index, filesystem[i])
        i += 1

    filesystem[i] = (-1, file_size)

# Calculate checksum
checksum = 0
counter = 0
for block in filesystem:
    block_id = block[0]
    block_size = block[1]

    counter += block_size
    if block_id == -1:
        continue

    checksum += block_id * (counter * block_size - sum(x for x in range(block_size + 1)))

print(checksum)
