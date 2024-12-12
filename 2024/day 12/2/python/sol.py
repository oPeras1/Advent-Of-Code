# Read input
with open('../../input.txt') as f:
    lines = [line for line in f.read().splitlines()]

def recursion_for_the_win(y, x, c, lines, visited_l):
    if (y, x) in visited_l:
        return (0, [])

    if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[0]):
        return (0, [(y, x)])
    if lines[y][x] != c:
        return (0, [(y, x)])
        
    visited_l.add((y, x))
    area = 1
    perimeter_coords = []
    
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = y + dy, x + dx
        sub_area, sub_perim = recursion_for_the_win(ny, nx, c, lines, visited_l)
        area += sub_area
        perimeter_coords.extend(sub_perim)
        
    return [area, perimeter_coords]

def check_alignment(coordm, coords):
    # Check for horizontal alignment (all y values the same)
    horizontal = all(coord[1] == coordm[1] for coord in coords)
    
    # Check for vertical alignment (all x values the same)
    vertical = all(coord[0] == coordm[0] for coord in coords)
    
    if horizontal:
        return True
    elif vertical:
        return True

    return False

def count_groups(coords):
    def get_neighbors(coord):
        x, y = coord
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    
    coords_list = list(coords)  # Convert to list if not already
    group_count = 0

    while coords_list:
        group_count += 1
        poped = coords_list.pop()
        stack = [poped]  # Start with last element
        alr_remvd = []
        alr_remvd.append(poped)
        while stack:
            current = stack.pop()
            neighbors = get_neighbors(current)
            
            # Find and remove neighbors that exist in coords_list
            i = 0
            while i < len(coords_list):
                if coords_list[i] in neighbors and coords_list[i] not in alr_remvd and check_alignment(coords_list[i], alr_remvd):
                    alr_remvd.append(coords_list[i])
                    stack.append(coords_list.pop(i))
                else:
                    i += 1

    return group_count

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

                sides = count_groups(area_perimeter[1])
                area_perimeter[1] = sorted(area_perimeter[1])
                print(lines[y][x], area_perimeter[0], sides, area_perimeter)
                total += area_perimeter[0] * sides
                
    return total

print(solve(lines))