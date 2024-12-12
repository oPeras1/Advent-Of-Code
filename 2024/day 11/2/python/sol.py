import math
from collections import defaultdict
import functools

stones = {}

with open('../../input.txt') as f:
    for num in f.read().split():
        stones[int(num)] = 1

# Hey! I just did this because in my head it is faster than do len(str(n))
@functools.lru_cache
def num_digits(n):
    return int(math.log10(abs(n))) + 1

for _ in range(75):
    
    nstones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            nstones[1] += count
        elif num_digits(stone)%2==0:
            div = 10**(num_digits(stone)//2)
            nstones[stone//div] += count
            nstones[stone%div] += count
        else:
            nstones[2024*stone] += count

    stones = nstones

count = 0
for _, c in stones.items():
    count += c

print(count)
