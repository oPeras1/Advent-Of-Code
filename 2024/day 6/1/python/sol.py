map_input = ""
with open("../../input.txt") as f:
    map_input = f.read()

    # Parse map and initialize variables
    grid = [list(line) for line in map_input.splitlines()]
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    
    # Find initial guard position and direction
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in directions:
                guard_pos = (row, col)
                guard_dir = grid[row][col]
                break
    
    while True:
        direction = directions[guard_dir]
        next_pos = (guard_pos[0] + direction[0], guard_pos[1] + direction[1])

        if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[0]):
            break

        if grid[next_pos[0]][next_pos[1]] == '#':
            guard_dir = turn_right[guard_dir]
        else:
            guard_pos = next_pos

        grid[guard_pos[0]][guard_pos[1]] = 'X'

    steps = 0
    for line in grid:
        for char in line:
            if char == 'X':
                steps += 1

    print("Steps:", steps)
