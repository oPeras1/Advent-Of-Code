locks = []
keys = []

lock = True

with open("input.txt") as f:
    th = []
    cnt = 0
    for line in f:
        cnt += 1

        if cnt == 1 and line[0] != "#":
            lock = False

        if cnt == 8:
            th = [list(x) for x in zip(*th)]
            if lock:
                locks.append(th)
            else:
                keys.append(th)
            th = []
            cnt = 0
            lock = True
        else:
            th.append(line.strip())

    th = [list(x) for x in zip(*th)]
    if lock:
        locks.append(th)
    else:
        keys.append(th)


count = 0
for lock in locks:
    pinlock = []
    for i in range(5):
        pinlock.append(lock[i].count("#"))

    for key in keys:
        pinkey = []
        for i in range(5):
            pinkey.append(key[i].count("#"))

        passed = True
        for i in range(5):
            if pinlock[i] + pinkey[i] > 7:
                passed = False
                break
            
        if passed:
            count += 1

print(count)
