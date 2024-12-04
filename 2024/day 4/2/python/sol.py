import re

with open("../../input.txt") as f:
    data = []
    for line in f:
        data.append(line.strip())
    
    word = "MAS"

    rows, cols = len(data), len(data[0])
    count = 0

    def is_xmas(x, y):
        if x - 1 < 0 or x + 1 >= rows or y - 1 < 0 or y + 1 >= cols:
            return False

        diag1 = [data[x - 1][y - 1], data[x][y], data[x + 1][y + 1]]
        diag2 = [data[x - 1][y + 1], data[x][y], data[x + 1][y - 1]]

        if ("".join(diag1) == word or "".join(diag1[::-1]) == word) and ("".join(diag2) == word or "".join(diag2[::-1]) == word):
            return True
        
        return False

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if is_xmas(i, j):
                count += 1

    print(count)
    
