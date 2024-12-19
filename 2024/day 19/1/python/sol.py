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
        return True

    if d in dp:
        return dp[d]

    for p in patterns:
        if d.startswith(p):
            if mk_design(d[len(p):]):
                dp[d] = True
                return True
    
    dp[d] = False
    return False

count = 0
for d in design:
    if mk_design(d):
        count += 1

print(count)