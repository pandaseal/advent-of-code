from collections import defaultdict

def main():

    cycles = parse_instructions('input.txt')
    
    print("Part 1:", signal_strength_sum(cycles))
    print("Part 2:")
    print_screen(CRT_screen(cycles))

def parse_instructions(filename):
    cycle = 1
    x = 1
    cycles = dict()
    
    with open(filename) as f:
        for line in f:
            cycles[cycle] = x
            cycle += 1
            match line.strip().split(): # instruction
                case 'addx', val:
                    cycles[cycle] = x
                    cycle += 1
                    x += int(val) # x is changed _after_ all cycles of the instruction are finished
                case ['noop']:
                    continue
    return cycles

def signal_strength_sum(cycles):
    strengths = []
    for c in [20, 60, 100, 140, 180, 220]:
        strengths.append(c * cycles[c])
    return sum(strengths)

# the CRT draws a single pixel during each cycle
def CRT_screen(cycles):
    height = 6
    width = 40
    screen = [['.' for _ in range(width)] for _ in range(height)]

    for i in range(1, len(cycles)):
        crt_pos =  (i-1) % width
        row = int(i/width)
        sprite_pos = [cycles[i]-1, cycles[i], cycles[i]+1]
        if crt_pos in sprite_pos:
            screen[row][crt_pos] = '#'
    return screen

def print_screen(screen):
    for row in screen:
        print(''.join(row))

if __name__ == "__main__":
    main()