from collections import deque

map2d = [["."] * 71 for _ in range(71)]

def bfs(start, goal):
    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        if (x, y) in visited:
            continue

        visited.add((x, y))
        
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 70 and 0 <= ny <= 70 and map2d[ny][nx] != "X":
                queue.append(((nx, ny), path + [(nx, ny)]))
    return None



coords = []
bts = 0
with open("../../input.txt") as file:
    for line in file:
        bts += 1
        x, y = line.strip().split(",")
        coords.append((int(x), int(y)))
        map2d[int(y)][int(x)] = "X"
        if bts >= 1024:
            path = bfs((0, 0), (70, 70))
            if not path:
                print(x, y)
                break
