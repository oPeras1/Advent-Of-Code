import re

with open("../../input.txt") as f:
    data = f.read()  # Read the entire file content

    part1, part2 = data.split("\n\n")

    data1 = [line.split('|') for line in part1.splitlines()]
    data1 = [[int(x) for x in pair] for pair in data1]  # Convert strings to integers

    # Process the second part into a single list of lists
    data2 = [list(map(int, group.split(','))) for group in part2.splitlines()]
    
    count = 0

    for update in data2:
        valid = True

        for pair in data1:
            val1 = pair[0]
            val2 = pair[1]
            if val1 in update and val2 in update:
                #get the index of val1 and val2
                index1 = update.index(val1)
                index2 = update.index(val2)
                if index1 > index2:
                    valid = False
                    break

        if valid:

            length = len(update)

            ## In my head length//2 + 1 is the middle element of the list. IT IS NOT, lost some minutes on this :cry:
            count += update[(length//2)]

    print(count)
            
    
    
