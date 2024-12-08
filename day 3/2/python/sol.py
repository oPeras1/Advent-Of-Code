import re

with open("../../input.txt") as f:
    # Regular expressions for valid instructions
    data = f.read()
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Initial state
    enabled = True
    sum = 0
    
    # Process instructions in order
    for match in re.finditer(f"{mul_pattern}|{do_pattern}|{dont_pattern}", data):
        instruction = match.group()
        
        if re.match(do_pattern, instruction):
            enabled = True
        elif re.match(dont_pattern, instruction):
            enabled = False
        elif enabled and re.match(mul_pattern, instruction):
            x, y = map(int, re.findall(r"\d{1,3}", instruction))
            sum += x * y
    
    print(sum)
