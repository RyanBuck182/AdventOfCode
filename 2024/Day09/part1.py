# Part One
# https://adventofcode.com/2024/day/9

with open("input.txt") as file:
    disk_map = file.read()

filesystem = []

# Creates the file system from the disk map
is_file = True
for i in range(len(disk_map)):
    if is_file:
        file_id = int(i / 2)
        file_size = int(disk_map[i])
        filesystem += [file_id for _ in range(file_size)]
    else:
        space_size = int(disk_map[i])
        filesystem += [-1 for _ in range(space_size)]

    is_file = not is_file

# Compresses the file system
space_index = -1
while space_index < len(filesystem) - 1:
    space_index += 1

    # Ensure we've found a free space
    if filesystem[space_index] != -1:
        continue

    # Remove free space at the end until the last element is data to be moved
    done_compressing = False
    for i in reversed(range(len(filesystem))):
        if filesystem[i] == -1:
            filesystem.pop()
            continue

        # If i goes past the space_index or the loop reaches completion,
        # we know there's no more free space left
        if i < space_index:
            done_compressing = True

        # We've either found our data or are done compressing
        break

    # Break if there's no more data to compress
    if done_compressing:
        break

    # Move the data to the free space
    filesystem[space_index] = filesystem.pop()

# Calculate checksum
checksum = 0
for i in range(len(filesystem)):
    checksum += i * filesystem[i]

print(checksum)
