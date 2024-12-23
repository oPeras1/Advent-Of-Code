network_map = {}
all_computers = set()

with open("../../input.txt", "r") as input_file:
    for entry in input_file:
        comp_a, comp_b = entry.strip().split("-")

        if comp_a not in network_map:
            network_map[comp_a] = []
        if comp_b not in network_map:
            network_map[comp_b] = []

        network_map[comp_a].append(comp_b)
        network_map[comp_b].append(comp_a)

        all_computers.update([comp_a, comp_b])

explored_paths = set()
longest_path = []

for starting_node in all_computers:
    search_stack = [(starting_node, [starting_node])]

    while search_stack:
        current_node, path_so_far = search_stack.pop()

        explored_paths.add(tuple(sorted(path_so_far)))

        if len(path_so_far) > len(longest_path):
            longest_path = path_so_far

        for adjacent_node in network_map[current_node]:
            is_fully_connected = all(adjacent_node in network_map[visited_node] for visited_node in path_so_far)

            if is_fully_connected:
                new_path = path_so_far + [adjacent_node]
                
                if tuple(sorted(new_path)) not in explored_paths:
                    search_stack.append((adjacent_node, new_path))

print(",".join(sorted(longest_path)))
