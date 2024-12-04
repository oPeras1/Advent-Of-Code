import re

with open("../../input.txt") as f:
    data = []
    for line in f:
        data.append(line.strip())
    
    word = "XMAS"

    rows, cols = len(data), len(data[0])
    word_len = len(word)
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1), 
    ]

    count = 0

    def is_valid(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols and data[nx][ny] == word[i]):
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if is_valid(i, j, dx, dy):
                    count += 1

    print(count)
    
