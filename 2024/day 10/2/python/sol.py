grid = []
zpos = []

with open("../../input.txt") as f:
    grid = [list(map(int, line)) for line in f.read().splitlines()]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                zpos.append([0, y, x])

count = 0

#BFS to make the path from 0 to 9
while len(zpos) > 0:
    new_zpos = []
    for z, y, x in zpos:
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= len(grid) or nx < 0 or nx >= len(grid[0]):
                continue
            if grid[ny][nx] == z+1:
                if z+1 == 9:
                    count += 1
                    continue
                new_zpos.append([z+1, ny, nx])
            
    zpos = new_zpos

print(count)