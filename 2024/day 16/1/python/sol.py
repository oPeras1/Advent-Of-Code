import heapq

map = []

with open("../../input.txt") as f:
    for line in f:
        map.append(list(line.strip()))

Spos = [0, 0, "^"]
Epos = [0, 0]

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "S":
            Spos = [y, x, "<"]
        if map[y][x] == "E":
            Epos = [y, x]

visited = set()
queue = [(0, Spos[0], Spos[1], Spos[2])]
directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

while queue:
    c, y, x, dira = heapq.heappop(queue)

    if y == Epos[0] and x == Epos[1]:
        print(c)
        break

    if (y, x, dira) in visited:
        continue

    visited.add((y, x, dira))

    dy = directions[dira][0]
    dx = directions[dira][1]
    ny, nx = y + dy, x + dx
    if 0 <= ny < len(map) and 0 <= nx < len(map[0]) and map[ny][nx] != "#":
        heapq.heappush(queue, (c + 1, ny, nx, dira))

    # Try all rotations
    for d in directions:
        if d != dira:  # Only rotate if it's a different direction
            heapq.heappush(queue, (c + 1000, y, x, d))