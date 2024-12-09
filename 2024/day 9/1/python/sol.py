with open('../../input.txt') as f:
    input = f.read()

lengths = [int(num) for num in input]


grid = []
for i, num in enumerate(lengths):
    for _ in range(num):
        if i % 2 == 0:
            grid.append(i//2)
        else:
            grid.append(-1)

while -1 in grid:
    val = grid[-1]
    if val == -1:
        grid.pop()
    else:
        i = grid.index(-1)
        grid[i] = val
        grid.pop()

sum = 0
for i in range(len(grid)):
    sum += grid[i] * (i)

print(sum)