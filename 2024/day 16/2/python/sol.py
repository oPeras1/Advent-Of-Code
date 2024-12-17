import heapq

map = []

with open("../../input.txt") as f:
    for line in f:
        map.append(list(line.strip()))

Spos = [0, 0, "<"]
Epos = [0, 0]

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "S":
            Spos = [y, x, "<"]
        if map[y][x] == "E":
            Epos = [y, x]

cost_so_far = {}
queue = [(0, Spos[0], Spos[1], Spos[2], [])]
directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

min_cost = -1
best_path_sets = set()

while queue:
    c, y, x, dira, path = heapq.heappop(queue)

    if (y, x, dira) in cost_so_far and c > cost_so_far[(y, x, dira)]:
        continue

    cost_so_far[(y, x, dira)] = c

    if y == Epos[0] and x == Epos[1]:
        if min_cost == -1 or c < min_cost:
            min_cost = c
            best_path_sets = set()

        if c > min_cost:
            count = 0

            break

        if c == min_cost:
            path.append((y, x))
            for p in path:
                best_path_sets.add(tuple(p))

        continue

    new_path = path + [(y, x)]

    dy, dx = directions[dira]
    ny, nx = y + dy, x + dx

    if 0 <= ny < len(map) and 0 <= nx < len(map[0]) and map[ny][nx] != "#":
        heapq.heappush(queue, (c + 1, ny, nx, dira, new_path))

    for d in directions:
        if d != dira:
            heapq.heappush(queue, (c + 1000, y, x, d, new_path))

print(len(best_path_sets))