def part1(): # After the rearrangement procedure completes, what crate ends up on top of each stack?
    with open('input.txt') as f:
        n_stacks = 0
        stack_mode = True
        stacks = {}
        for line in f:
            if stack_mode:
                if n_stacks == 0: # first row
                    n_stacks = int(len(line)/4)

                    # init stacks data structures
                    for i in range(n_stacks):
                        stacks[i+1] = []
                
                # fill stacks data structures
                for i in range(n_stacks):
                    crate = line[(i*4)+1]
                    if crate == "1":
                        stack_mode = False
                        break
                    else:
                        if not (crate == ' '):
                            stacks[i+1].insert(0, crate)

            else:
                # read and execute instruction
                if not (len(line) == 1):
                    n, fr, to = get_instr(line)

                    for i in range(n):
                        crate = stacks[fr].pop()
                        stacks[to].append(crate)
        
        print("Part 1:", get_top_crates(stacks))

def part2(): # After the rearrangement procedure completes, what crate ends up on top of each stack?
    with open('input.txt') as f:
        n_stacks = 0
        stack_mode = True
        stacks = {}
        for line in f:
            if stack_mode:
                if n_stacks == 0: # first row
                    n_stacks = int(len(line)/4)

                    # init stacks data structures
                    for i in range(n_stacks):
                        stacks[i+1] = []
                
                # fill stacks data structures
                for i in range(n_stacks):
                    crate = line[(i*4)+1]
                    if crate == "1":
                        stack_mode = False
                        break
                    else:
                        if not (crate == ' '):
                            stacks[i+1].insert(0, crate)

            else:
                # read and execute instruction
                if not (len(line) == 1):
                    n, fr, to = get_instr(line)

                    stacks[to].extend(stacks[fr][-n:])
                    del stacks[fr][-n:]
        
        print("Part 2:", get_top_crates(stacks))

def get_instr(line):
    instr = line.strip().split()
    n = int(instr[1])
    fr = int(instr[3])
    to = int(instr[5])
    return n, fr, to

def get_top_crates(stacks):
    on_top = ''
    for i in range(len(stacks)):
        on_top += stacks[i+1].pop()
    return on_top


if __name__ == "__main__":
    #part1()
    part2()
