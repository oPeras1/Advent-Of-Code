from collections import defaultdict

with open("../../input.txt") as fin:
    grid = [list(line.strip()) for line in fin.readlines()]


N = len(grid)
def in_grid(i, j):
    return 0 <= i < N and 0 <= j < N

si = sj = ei = ej = ""
for i in range(N):
    for j in range(N):
        if grid[i][j] == "S":
            si, sj = i, j
        elif grid[i][j] == "E":
            ei, ej = i, j

dd = [[1, 0], [0, 1], [-1, 0], [0, -1]]

path = [(si, sj)]
while path[-1] != (ei, ej):
    i, j = path[-1]
    for di, dj in dd:
        ii, jj = i + di, j + dj
        if not in_grid(ii, jj):
            continue
        if len(path) > 1 and (ii, jj) == path[-2]:
            continue
        if grid[ii][jj] == "#":
            continue
        
        path.append((ii, jj))
        break

og = len(path) - 1

times = {}
for t, coord in enumerate(path):
    times[coord] = og - t

counts = defaultdict(int)
saved = {}

for t, coord in enumerate(path):
    i, j = coord
    for di1, dj1 in dd:
        for di2, dj2 in dd:
            ii, jj = i + di1 + di2, j + dj1 + dj2
            if not in_grid(ii, jj) or grid[ii][jj] == "#":
                continue

            rem_t = times.get((ii, jj), 0)
            saved[(i, j, ii, jj)] = og - (t + rem_t + 2)

count = 0
for v in saved.values():
    if v >= 0: counts[v] += 1
    if v >= 100: count += 1

print(count)