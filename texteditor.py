import sys

MAX_memory = 65536
mem = []
pointer_instruction = 0
pointer_mem = 0

for i in range(MAX_memory):
    mem.append(0)

loops = []

program = list(open(sys.argv[1]).read())

while pointer_instruction != len(program):
    instruction = program[pointer_instruction]
    if instruction == "+":
        mem[pointer_mem] += 1

    elif instruction == "-":
        mem[pointer_mem] -= 1

    elif instruction == "<":
        pointer_mem -= 1

    elif instruction == ">":
        pointer_mem += 1






    elif instruction == ".":
        print(chr(mem[pointer_mem]), end="")

    elif instruction == ",":
        mem[pointer_mem] = int(ord(input("")[0]))

    elif instruction == "[":
        loops.append(pointer_instruction)

    elif instruction == "]":
        if mem[pointer_mem] == 0:
            loops.pop()

        else:
            pointer_instruction = loops[-1]

    pointer_instruction += 1