import re

with open("../../input.txt") as f:
    data = f.read()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)

    sum = 0
    for x,y in matches:
        sum += int(x) * int(y)

    print(sum)
