patterns = []

design = []

with open('../../input.txt') as f:
    patterns = f.readline().strip().split(', ')

    for line in f:
        if line.strip() == '':
            continue
        design.append(line.strip())

dp = {}

def mk_design(d):
    if d == "":
        return 1

    if d in dp:
        return dp[d]

    count = 0
    for p in patterns:
        if d.startswith(p):
            count += mk_design(d[len(p):])
    
    dp[d] = count
    return count

count = 0
for d in design:
    count += mk_design(d)

print(count)