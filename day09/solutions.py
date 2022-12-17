from math import dist, sqrt

def main():
    #part1()
    part2()

# Simulate your complete hypothetical series of motions. 
# How many positions does the tail of the rope visit at least once?
def part1():

    head = (0, 0)
    tail = (0, 0)

    tail_history = set()
    tail_history.add(tail)

    with open('input.txt') as f:
        for line in f:
            head, tail, tail_history = move2knots(line.strip().split(), head, tail, tail_history)

    print("Part 1:", len(tail_history))

def part2():

    rope = [(0, 0) for _ in range(10)]

    tail_history = set()
    tail_history.add(rope[-1])

    with open('input.txt') as f:
        for line in f:
            rope, tail_history = move10knots(line.strip().split(), rope, tail_history)

    print("Part 2:", len(tail_history))

def move10knots(motion, rope, tail_history):
    for _ in range(int(motion[1])):
        new_rope = rope.copy()

        # move head
        new_rope[0] = move(rope[0], motion[0])

        # move all knots below head
        for i in range(1, len(rope)):
            if dist(new_rope[i-1], rope[i]) > sqrt(2):
                new_rope[i] = shortest_possible_move(new_rope[i-1], rope[i])

        tail_history.add(new_rope[-1])
        rope = new_rope.copy()

    return rope, tail_history

def shortest_possible_move(target_pos, init_pos):
    # generate possible moves
    possible_new_pos = possible_moves(init_pos)

    # placeholders
    closest_new_pos = init_pos
    current_dist = dist(target_pos, init_pos)

    # measure distance to tagret for each move
    for possible_pos in possible_new_pos:
        new_dist = dist(possible_pos, target_pos)
        if new_dist < current_dist:
            closest_new_pos = possible_pos
            current_dist = new_dist

    return closest_new_pos

# straight and diagonal
def possible_moves(pos):
    x, y = pos
    possible_pos = []
    possible_pos.append((x, y+1)) # up
    possible_pos.append((x, y-1)) # down
    possible_pos.append((x-1, y)) # left
    possible_pos.append((x+1, y)) # right
    possible_pos.append((x-1, y+1)) # up-left
    possible_pos.append((x+1, y+1)) # up-right
    possible_pos.append((x-1, y-1)) # down-left
    possible_pos.append((x+1, y-1)) # down-right
    return possible_pos

def visualize_small_example(rope):
    grid = [['.' for _ in range(6)] for _ in range(5)]
    indexed_rope = list(zip(rope, range(len(rope))))
    indexed_rope.reverse()

    for ((x, y), i) in indexed_rope:
        if i == 0:
            grid[y][x] = 'H'
        else:
            grid[y][x] = str(i)
    grid.reverse()
    for line in grid:
        print(' '.join(line))
    print()

def move2knots(motion, head, tail, tail_history):
    for _ in range(int(motion[1])):
        new_head = move(head, motion[0])
        if dist(new_head, tail) > sqrt(2):
            tail = head
            tail_history.add(tail)
        head = new_head
    return head, tail, tail_history   

# performs the move of one point, 
# one step in a given direction
# assumes 2D point in form of tuple
def move(point, direction):
    match direction:
        case 'L':
            return (point[0]-1, point[1])
        case 'R':
            return (point[0]+1, point[1])
        case 'U':
            return (point[0], point[1]+1)
        case 'D':
            return (point[0], point[1]-1)
        case other:
            print("No match found for direction!")
            return point
            
if __name__ == "__main__":
    main()