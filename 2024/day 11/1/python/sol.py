import math

stones = []

with open('../../input.txt') as f:
    stones = [int(num) for num in f.read().split()]

# Hey! I just did this because in my head it is faster than do len(str(n))
def num_digits(n): 
    return int(math.log10(abs(n))) + 1

for _ in range(25):
    nstone = []

    for stone in stones:
        if stone == 0:
            nstone.append(1)
        elif num_digits(stone)%2==0:
            div = 10**(num_digits(stone)//2)
            nstone.append(stone//div)
            nstone.append(stone%div)
        else:
            nstone.append(2024*stone)

    stones = nstone

print(len(stones))

