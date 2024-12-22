from collections import deque
from functools import cache
from itertools import product

dir = [[-1, 0, "^"], [1, 0, "v"], [0, -1, "<"], [0, 1, ">"]]

def generate_sequences(key_layout):
    key_positions = {}
    for row in range(len(key_layout)):
        for col in range(len(key_layout[row])):
            if key_layout[row][col] != "":
                key_positions[key_layout[row][col]] = (row, col)

    key_combinations = {}
    for start_key in key_positions:
        for end_key in key_positions:
            if start_key == end_key:
                key_combinations[(start_key, end_key)] = ["A"]
                continue

            possible_sequences = []
            queue = deque([(key_positions[start_key], "")])
            shortest_path = float("inf")

            while queue:
                (current_row, current_col), path = queue.popleft()
                for row, col, move in dir:
                    new_row = current_row + row
                    new_col = current_col + col
                    if (new_row < 0 or new_col < 0 or new_row >= len(key_layout) or new_col >= len(key_layout[0]) or key_layout[new_row][new_col] == ""):
                        continue

                    if key_layout[new_row][new_col] == end_key:
                        if shortest_path < len(path) + 1:
                            break
                        shortest_path = len(path) + 1
                        possible_sequences.append(path + move + "A")
                    else:
                        queue.append(((new_row, new_col), path + move))
                        
                else:
                    continue

                break

            key_combinations[(start_key, end_key)] = possible_sequences
    return key_combinations

def calculate_combinations(input_string, key_sequences):
    sequence_options = [key_sequences[(start, end)] for start, end in zip("A" + input_string, input_string)]
    return ["".join(option) for option in product(*sequence_options)]

numeric_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["", "0", "A"]
]

numeric_sequences = generate_sequences(numeric_keypad)

directional_keypad = [
    ["", "^", "A"],
    ["<", "v", ">"]
]

directional_sequences = generate_sequences(directional_keypad)
directional_lengths = {key: len(value[0]) for key, value in directional_sequences.items()}

@cache
def cached_computation(sequence, depth=25):
    if depth == 1:
        return sum(directional_lengths[(start, end)] for start, end in zip("A" + sequence, sequence))

    total_length = 0
    for start, end in zip("A" + sequence, sequence):
        total_length += min(
            cached_computation(sub_sequence, depth - 1)
            for sub_sequence in directional_sequences[(start, end)]
        )
    return total_length

total_score = 0

with open("../../input.txt") as file:
    input_lines = file.read().splitlines()

for line in input_lines:
    sequence_variants = calculate_combinations(line, numeric_sequences)
    minimum_length = min(map(cached_computation, sequence_variants))

    total_score += minimum_length * int(line[:-1])

print(total_score)