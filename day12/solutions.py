from collections import deque

'''
    # forward: neighbors can at most be +1 higher than the current node
    # backwards: neighbors can at most be -1 lower than the current node
'''
def get_neighbors(heightmap, lookup, pos, start, forward=True):
    height = get_height(lookup, heightmap, pos)
    row, col = pos
    adjacent_pos = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
    reachable_neighbors = []
    for n_pos in adjacent_pos:
        if pos_within_grid(n_pos, heightmap):
            if n_pos != start:
                neighbor_height = get_height(lookup, heightmap, n_pos)
                if forward:
                    if neighbor_height <= height+1:
                        reachable_neighbors.append(n_pos)
                else:
                    if neighbor_height >= height-1:
                        reachable_neighbors.append(n_pos)
    return reachable_neighbors

def pos_within_grid(pos, heightmap):
    max_row = len(heightmap)-1
    max_col = len(heightmap[0])-1
    r, c = pos
    return (0 <= r <= max_row) and (0 <= c <= max_col)


def get_height(lookup, heightmap, pos):
    row, col = pos
    return lookup[heightmap[row][col]]

'''
    "Your current position (S) has elevation a (1), 
    and the location that should get the best signal (E) has elevation z (26)."
'''
def generate_lookup():
    lookup = dict([(char, num+1) for num, char in enumerate('abcdefghijklmnopqrstuvwxyz')])
    lookup['S'] = 1     # elevation a
    lookup['E'] = 26    # elevation z
    return lookup

def get_single_index(char, heightmap):
    for row, elements in enumerate(heightmap):
        col  = [index for (index, item) in enumerate(elements) if item == char]
        if col != []:
            return (row, col[0])
        
def get_all_index(char, heightmap):
    index = []
    for row, row_elements in enumerate(heightmap):
        for col in [index for (index, item) in enumerate(row_elements) if item == char]:
            index.append((row, col))
    return index
        
def bfs(adjacency_list, start, end_list):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append((start, 0))

    while queue:
        node, dist = queue.popleft()
        if node in end_list:
            return dist
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist+1))
    return -1

def read_input(filename):
    heightmap = []
    with open(filename) as f:
        for line in f:
            l = list(line.strip())
            heightmap.append(l)
    return heightmap

'''
    # adjacency list:
    # - coordinates/ID,
    # - reachable neighbors
    # - remove neighbors that are S or are too high up
'''
def get_adjacency_list(heightmap, height_lookup, start_index, forward=True):
    adjacency_list = dict()
    for row, row_elements in enumerate(heightmap):
        for col, _ in enumerate(row_elements):
            node = (row, col)
            adjacency_list[node] = get_neighbors(heightmap, height_lookup, node, start_index, forward)
    return adjacency_list

'''
What is the fewest steps required to move from your current 
position (S) to the location that should get the best signal (E)?
'''
def part_one(heightmap, height_lookup):
    start = get_single_index('S', heightmap)
    end = get_single_index('E', heightmap)
    adjacency_list = get_adjacency_list(heightmap, height_lookup, start, forward=True)

    print("part 1:", bfs(adjacency_list, start, [end]))

'''
What is the fewest steps required to move starting from any square 
with elevation a to the location that should get the best signal (E)?

    # always start at 'E'
    # stop when first 'a' is found
    # return that distance

    # current node can only be +1 higher than neighbors
    # reverse adjacency list
    # alter neigbor criteria
'''
def part_two(heightmap, height_lookup):
    start = get_single_index('E', heightmap)
    end_alts = get_all_index('a', heightmap)
    adjacency_list = get_adjacency_list(heightmap, height_lookup, start, forward=False)
    
    print("part 2:", bfs(adjacency_list, start, end_alts))

if __name__ == "__main__":
    filename='input.txt'
    heightmap = read_input(filename)
    height_lookup = generate_lookup()

    part_one(heightmap, height_lookup)
    part_two(heightmap, height_lookup)