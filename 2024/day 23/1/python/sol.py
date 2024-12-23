network_map = {}
all_computers = set()

with open("../../input.txt", "r") as file:
    for line in file:
        node_a, node_b = line.strip().split("-")

        network_map.setdefault(node_a, []).append(node_b)
        network_map.setdefault(node_b, []).append(node_a)

        all_computers.update([node_a, node_b])

sets = set() 

for start in all_computers:
    stack = [(start, set())] 

    while stack:
        current, visited = stack.pop()
        visited.add(current)

        if len(visited) > 3:
            continue

        for neighbor in network_map[current]:
            if neighbor in visited:
                if len(visited) == 3 and neighbor == start:
                    sorted_path = sorted(visited)
                    if any(code.startswith("t") for code in sorted_path):
                        sets.add(tuple(sorted_path))
                continue

            stack.append((neighbor, visited.copy()))

print(len(sets))
