def get_gen(num, times):
    for i in range(times):
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

count = 0
for n in nlist:
    count += get_gen(n, 2000)

print(count)