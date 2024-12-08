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

            sum = (xdif, ydif)

            for l in range(2):
                uniqueantinode.add(a1)

                antinode = (a1[0] + sum[0], a1[1] + sum[1])
                
                while True:
                    
                    if antinode[0] >= 0 and antinode[0] < len(lines) and antinode[1] >= 0 and antinode[1] < len(lines[0]):
                        uniqueantinode.add(antinode)
                    else:
                        break

                    antinode = (antinode[0] + sum[0], antinode[1] + sum[1])
                    
                sum = (-sum[0], -sum[1])

print(len(uniqueantinode))
            

                