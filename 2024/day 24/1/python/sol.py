mathsuper = {}

operations = []

after = False
with open('../../input.txt') as f:
    for line in f:
        line = line.strip()
        if line == '':
            after = True
            continue

        if not after:
            splitting = line.split(": ")

            varname = splitting[0]
            value = splitting[1]

            mathsuper[varname] = int(value)
        else:
            splitting = line.split(" ")
            varname1 = splitting[0]
            varname2 = splitting[2]
            operator = splitting[1]

            varname3 = splitting[4]

            operations.append([varname1, varname2, operator, varname3])


queue = []

queue.append(operations[0])

k = 0

visited = set()

while len(queue) > 0:
    k += 1
    queueitem = queue.pop(0)

    varname1 = queueitem[0]
    varname2 = queueitem[1]

    if varname1 in mathsuper and varname2 in mathsuper:
        if queueitem[2] == "AND":
            mathsuper[queueitem[3]] = int(mathsuper[varname1] and mathsuper[varname2])
        elif queueitem[2] == "OR":
            mathsuper[queueitem[3]] = int(mathsuper[varname1] or mathsuper[varname2])
        elif queueitem[2] == "XOR":
            if mathsuper[varname1] and mathsuper[varname2]:
                mathsuper[queueitem[3]] = 0
            elif mathsuper[varname1] or mathsuper[varname2]:
                mathsuper[queueitem[3]] = 1
            else:
                mathsuper[queueitem[3]] = 0

        visited.add((queueitem[0], queueitem[1], queueitem[2], queueitem[3]))
        
    else:
        if varname1 not in mathsuper:
            for operation in operations:
                if operation[3] == varname1:
                    queue.append(operation)
                    break
        
        if varname2 not in mathsuper:
            for operation in operations:
                if operation[3] == varname2:
                    queue.append(operation)
                    break

        queue.append(queueitem)
    
    if k < len(operations):
        qnext = (operations[k][0], operations[k][1], operations[k][2], operations[k][3])

        if qnext not in visited:
            queue.append(qnext)

mathsuper = {k: mathsuper[k] for k in sorted(mathsuper)}

binnumber = ""
for v in reversed(mathsuper):
    if v[0] == "z":
        binnumber += str(mathsuper[v])

print(int(binnumber, 2))