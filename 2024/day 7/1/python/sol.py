with open("../../input.txt") as f:
    lines = [line for line in f.read().splitlines()]

equations = []
for line in lines:
    result, numbers = line.split(":")
    equations.append((int(result), [*map(int, numbers.strip().split())]))

result = []

for r, numbers in equations:
    possibles = [numbers.pop(0)]
    while numbers:
        curr = numbers.pop(0)
        temp = []
        for p in possibles:
            temp.append(p + curr)
            temp.append(p * curr)
        possibles = temp

    if r in possibles:
        result.append(r)

count = 0
for r in result:
    count += r

print(count)