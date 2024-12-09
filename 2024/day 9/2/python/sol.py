with open('../../input.txt') as f:
    input = f.read()

lengths = [int(num) for num in input]

grid = []
for i, num in enumerate(lengths):
    for _ in range(num):
        if i % 2 == 0:
            grid.append(i//2)
        else:
            grid.append(-1)

fsize = {}
for i in range(0, len(lengths), 2):
    fsize[i//2] = lengths[i]

maxid = max(fsize.keys())
for fid in range(maxid, -1, -1):
    startpos = -1
    size = fsize[fid]
    
    for i in range(len(grid)):
        if grid[i] == fid:
            startpos = i
            break
            
    if startpos == -1:
        continue
        
    bestpos = -1
    current_free = 0
    for i in range(startpos):
        if grid[i] == -1:
            current_free += 1
            if current_free == size and bestpos == -1:
                bestpos = i - size + 1
        else:
            current_free = 0
            
    if bestpos != -1:
        for i in range(size):
            grid[bestpos + i] = fid
        for i in range(startpos, startpos + size):
            grid[i] = -1

sum = 0
for i in range(len(grid)):
    if grid[i] != -1:
        sum += grid[i] * i

print(sum)