def get_gen(num):
    m = num*64
    num = m ^ num
    num = num % 16777216

    m = num//32
    m = round(m)
    num = m ^ num
    num = num % 16777216

    m = num*2048
    num = m ^ num
    num = num % 16777216
    
    return num

nlist = []

with open("../../input.txt", "r") as file:
    for line in file:
        nlist.append(int(line.strip()))

seqend = {}

for num in nlist:
    buyer = []
    for _ in range(2000):
        buyer.append(num % 10)
        num = get_gen(num)
        
    buyer.append(num % 10)

    visited = set()

    for i in range(len(buyer) - 4):
        a, b, c, d, e = buyer[i:i + 5]
        seq = (b - a, c - b, d - c, e - d)

        if seq in visited:
            continue

        visited.add(seq)

        if seq not in seqend:
            seqend[seq] = 0

        seqend[seq] += e

max = 0
for k, v in seqend.items():
    if v > max:
        max = v

print(max)