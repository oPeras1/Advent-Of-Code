map = []

directions = ""
with open("../../input.txt", "r") as file:
    for line in file:
        # until the line is empty
        if line.strip() == "":
            # read the REST of the file to directions (except the last newline)
            directions = file.read().strip()
            break
        newmaps = []
        for char in line.strip():
            if char == "#":
                newmaps.append("#")
                newmaps.append("#")
            elif char == "@":
                newmaps.append("@")
                newmaps.append(".")
            elif char == "O":
                newmaps.append("[")
                newmaps.append("]")
            elif char == ".":
                newmaps.append(".")
                newmaps.append(".")
        map.append(newmaps)

directions = ''.join(char for char in directions if char in '^v<>')

def get_connected_boxes(poss, go):
    y, x = poss

    connected_boxes = {(y, x, map[y][x])}
    queue = [(y, x)]

    if map[y][x] == "[":
        connected_boxes.add((y, x+1, map[y][x+1]))
        queue.append((y, x+1))
    elif map[y][x] == "]":
        connected_boxes.add((y, x-1, map[y][x-1]))
        queue.append((y, x-1))

    while queue:
        cy, cx = queue.pop(0)
        dy, dx = go
        ny, nx = cy + dy, cx + dx
        while (map[ny][nx] == '[' or map[ny][nx] == ']'):
            if (ny, nx) not in connected_boxes:
                connected_boxes.add((ny, nx, map[ny][nx]))
                queue.append((ny, nx))

                if map[ny][nx] == "[":
                    connected_boxes.add((ny, nx+1, map[ny][nx+1]))
                    queue.append((ny, nx+1))
                elif map[ny][nx] == "]":
                    connected_boxes.add((ny, nx-1, map[ny][nx-1]))
                    queue.append((ny, nx-1))

            ny += dy
            nx += dx

        if map[ny][nx] == "#":
            connected_boxes.add((ny, nx, "#"))

    return connected_boxes


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


    if char in "<>":
        if map[new_pos[0]][new_pos[1]] in "[]":
            box = new_pos
            while map[box[0]][box[1]] in "[]":
                who.append([box[0], box[1], map[box[0]][box[1]]])
                box = [box[0] + go[0], box[1] + go[1]]

            if map[box[0]][box[1]] == "#":
                continue
    else:
        if map[new_pos[0]][new_pos[1]] in "[]":
            who = get_connected_boxes(new_pos, go)

            if any(pos[2] == "#" for pos in who):
                continue



    for point in who:
        map[point[0]][point[1]] = "."

    for point in who:
        new_point = [point[0] + go[0], point[1] + go[1]]
        map[new_point[0]][new_point[1]] = point[2]

    map[pos[0]][pos[1]] = "."
    pos = new_pos
    map[pos[0]][pos[1]] = "@"


count = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "[":
            count = count + 100*y + x


print(count)
        
        