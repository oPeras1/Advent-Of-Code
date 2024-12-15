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
            robots.append([px, py, vx, vy])

grid = []
for _ in range(103):
    grid.append([" "]*101)

count = 0
while True:
    for robot in robots:
        grid[robot[1]][robot[0]] = " "
        robot[0] = (robot[0]+robot[2])%101
        robot[1] = (robot[1]+robot[3])%103
        grid[robot[1]][robot[0]] = "#"

    #check if there is 10 robots in a row
    count += 1
    for y in range(103):
        for x in range(101):
            if grid[y][x] == "#":
                if x + 10 < 101 and all(grid[y][x+i] == "#" for i in range(10)):
                    print(count)
                    print("".join("".join(str(x) for x in row) + "\n" for row in grid))
                    break
                elif y + 10 < 103 and all(grid[y+i][x] == "#" for i in range(10)):
                    print(count)
                    print("".join("".join(str(x) for x in row) + "\n" for row in grid))
                    break


    
