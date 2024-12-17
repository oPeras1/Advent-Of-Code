from collections import deque

A = 47792830
B = 0
C = 0

prog = [2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0]

output = []


def combo(op):
    global A, B, C, output
    if 0 <= op <= 3:
        return op

    if op == 4:
        return A

    if op == 5:
        return B

    if op == 6:
        return C

def instruction(opcode, plus):
    global A, B, C, output

    if opcode == 0:
        A = A//(2**combo(plus))
        return
    
    if opcode == 1:
        B = B ^ plus

        return

    if opcode == 2:
        B = combo(plus) % 8
        return

    if opcode == 3:
        if A == 0:
            return
        
        return plus

    if opcode == 4:
        B = B ^ C
        return

    if opcode == 5:
        output.append(combo(plus)%8)

    if opcode == 6:
        B = A//(2**combo(plus))
        return

    if opcode == 7:
        C = A//(2**combo(plus))
        return


def run(a, b, c, p):
    global A, B, C, output
    output = []
    A = a
    B = b
    C = c
    prog = p
    i = 0
    while (i < len(prog)):
        opcode = prog[i]
        plus = prog[i+1]
        retvalue = instruction(opcode, plus)
        if retvalue != None:
            i = retvalue
        else:
            i += 2

    return output

def reveng(program, a, b, c, prg_pos):
    if abs(prg_pos) > len(program):
        return a

    for i in range(8):
        fout = run(a * 8 + i, b, c, program)[0]
        if fout == program[prg_pos]:
            e = reveng(program, a * 8 + i, b, c, prg_pos - 1)
            if e:
                return e



print(reveng(prog, 0, B, C, -1))
