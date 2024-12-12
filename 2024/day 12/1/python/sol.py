# Read input
with open('../../input.txt') as f:
    lines = [line for line in f.read().splitlines()]

def recursion_for_the_win(y, x, c, lines, visited_l):
    if (y, x) in visited_l:
        return (0, 0)

    if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[0]):
        return (0, 1)
    if lines[y][x] != c:
        return (0, 1)
        
    visited_l.add((y, x))
    area = 1
    perimeter = 0
    
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = y + dy, x + dx
        sub_area, sub_perim = recursion_for_the_win(ny, nx, c, lines, visited_l)
        area += sub_area
        perimeter += sub_perim
        
    return (area, perimeter)

def solve(lines):
    total = 0
    visited_global = set()
    
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if (y, x) in visited_global:
                continue
                
            visited_local = set()
            area_perimeter = recursion_for_the_win(y, x, lines[y][x], lines, visited_local)
            
            if area_perimeter[0] > 0:
                visited_global.update(visited_local)
                total += area_perimeter[0] * area_perimeter[1]
                
    return total

print(solve(lines))