import re

# Original input list remains
robots = []

with open("../../input.txt", "r") as file:
    for line in file:
        # Extract position and velocity using regex
        pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
        match = re.match(pattern, line.strip())
        if match:
            px, py, vx, vy = map(int, match.groups())
            robots.append((px, py, vx, vy))

grid = []
for _ in range(103):
    grid.append([0]*101)

for robot in robots:
    posx = (robot[0]+robot[2]*100)%101
    posy = (robot[1]+robot[3]*100)%103
    grid[posy][posx] += 1

s1 = sum(grid[y][x] for y in range(0,51) for x in range(0,50))
s2 = sum(grid[y][x] for y in range(0,51) for x in range(51,101))
s3 = sum(grid[y][x] for y in range(52,103) for x in range(0,50))
s4 = sum(grid[y][x] for y in range(52,103) for x in range(51,101))

print(s1*s2*s3*s4)
