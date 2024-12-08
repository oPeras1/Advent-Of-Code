map_input = ""
with open("../../input.txt") as f:
    map_input = f.read()

def simulate_with_obstruction(map_data, new_obstruction):
    # Parse map and initialize variables
    grid = [list(row) for row in map_data.splitlines()]
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    # Add the new obstruction
    r, c = new_obstruction
    grid[r][c] = '#'
    
    # Find initial guard position and direction
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in directions:
                guard_pos = (row, col)
                guard_dir = grid[row][col]
                break
    
    visited_states = set() 
    rows, cols = len(grid), len(grid[0])
    
    while True:
        state = (guard_pos, guard_dir)
        
        if state in visited_states:
            return True
        visited_states.add(state)
        
        r, c = guard_pos
        dr, dc = directions[guard_dir]
        next_pos = (r + dr, c + dc)
        
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break
        
        if grid[next_pos[0]][next_pos[1]] == '#':
            guard_dir = turn_right[guard_dir]
        else:
            guard_pos = next_pos 
    
    return False


grid = [list(row) for row in map_data.splitlines()]
rows, cols = len(grid), len(grid[0])
possible_positions = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '.':
            if simulate_with_obstruction(map_data, (r, c)):
                possible_positions += 1

print("Loops:", find_obstruction_positions(map_input))
