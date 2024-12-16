map = []

directions = ""
with open("../../input.txt", "r") as file:
    for line in file:
        # until the line is empty
        if line.strip() == "":
            # read the REST of the file to directions (except the last newline)
            directions = file.read().strip()
            break
        map.append(list(line.strip()))

directions = ''.join(char for char in directions if char in '^v<>')

# Find the starting position

dir = {">": [0, 1], "<": [0, -1], "^": [-1, 0], "v": [1, 0]}
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "@":
            pos = [y, x]

for char in directions:
    go = dir[char]

    who = []

    new_pos = [pos[0] + go[0], pos[1] + go[1]]

    if map[new_pos[0]][new_pos[1]] == "#":
        continue


    if map[new_pos[0]][new_pos[1]] == "O":
        box = new_pos
        while map[box[0]][box[1]] == "O":
            who.append(box)
            box = [box[0] + go[0], box[1] + go[1]]

        if map[box[0]][box[1]] == "#":
            continue


    # move every point in who in the direction of go
    for point in who:
        map[point[0]][point[1]] = "."

    for point in who:
        new_point = [point[0] + go[0], point[1] + go[1]]
        map[new_point[0]][new_point[1]] = "O"

    map[pos[0]][pos[1]] = "."
    pos = new_pos
    map[pos[0]][pos[1]] = "@"

count = 0
for y in range(len(map)):
    for x in range(len(map[x])):
        if map[y][x] == "O":
            count = count + 100*y + x


print(count)
        
        