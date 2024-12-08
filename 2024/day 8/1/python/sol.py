with open("../../input.txt") as f:
    lines = [line for line in f.read().splitlines()]

antenas = {}

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != ".":
            if lines[i][j] not in antenas:
                antenas[lines[i][j]] = [(i, j)]
            else:
                antenas[lines[i][j]].append((i, j))

uniqueantinode = set()

for a in antenas:
    for i in range(len(antenas[a])):
        for j in range(i+1, len(antenas[a])):
            a1 = antenas[a][i]
            a2 = antenas[a][j]

            xdif = a1[0] - a2[0]
            ydif = a1[1] - a2[1]

            antinode1 = (a1[0] + xdif, a1[1] + ydif)
            if antinode1[0] == a2[0] and antinode1[1] == a2[1]:
                antinode1 = (a1[0] - xdif, a1[1] - ydif)

            antinode2 = (a2[0] + xdif, a2[1] + ydif)
            if antinode2[0] == a1[0] and antinode2[1] == a1[1]:
                antinode2 = (a2[0] - xdif, a2[1] - ydif)
            

            if antinode1[0] >= 0 and antinode1[0] < len(lines) and antinode1[1] >= 0 and antinode1[1] < len(lines[0]):
                uniqueantinode.add(antinode1)

            if antinode2[0] >= 0 and antinode2[0] < len(lines) and antinode2[1] >= 0 and antinode2[1] < len(lines[0]):
                uniqueantinode.add(antinode2)

print(len(uniqueantinode))
            

                