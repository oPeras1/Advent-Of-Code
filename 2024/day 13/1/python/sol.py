import re

def get_tokens(button_a, button_b, prize):
    # Deophantines equations
    # If we have the determinants of the matrixes, we can solve the equations very easily
    # EMD foi útil? 
    
    n1 = (prize[0]*button_b[1] - prize[1]*button_b[0]) / (button_a[0]*button_b[1] - button_a[1]*button_b[0])
    n2 = (prize[1]*button_a[0] - prize[0]*button_a[1]) / (button_a[0]*button_b[1] - button_a[1]*button_b[0])

    if n1 % 1 == 0 and n2 % 1 == 0 and n1 >= 0 and n2 >= 0:
        return int(n1*3 + n2)

    return 0

machines = []

with open('../../input.txt') as f:
    data = f.read()

pattern = re.compile(
    r"Button A: X\+([0-9]+), Y\+([0-9]+)\s*"
    r"Button B: X\+([0-9]+), Y\+([0-9]+)\s*"
    r"Prize: X=([0-9]+), Y=([0-9]+)"
)
matches = pattern.findall(data)

for match in matches:
    button_a = (int(match[0]), int(match[1]))
    button_b = (int(match[2]), int(match[3]))
    prize = (int(match[4]), int(match[5]))
    machines.append((button_a, button_b, prize))

count = 0

for machine in machines:
    button_a, button_b, prize = machine
    solution = get_tokens(button_a, button_b, prize)
    count += solution

print(count)