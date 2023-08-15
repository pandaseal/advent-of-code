from collections import deque

def get_neighbors(heightmap, lookup, pos, start):
    max_row = len(heightmap)-1
    max_col = len(heightmap[0])-1

    height = get_height(lookup, heightmap, pos)
    row, col = pos
    adjacent_pos = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
    reachable_neighbors = []
    for r, c in adjacent_pos:
        if (0 <= r <= max_row) and (0 <= c <= max_col):
            n_pos = (r, c)
            if n_pos != start:
                neighbor_height = get_height(lookup, heightmap, n_pos)
                if neighbor_height <= height+1:
                    reachable_neighbors.append(n_pos)
    return reachable_neighbors

def get_height(lookup, heightmap, pos):
    row, col = pos
    return lookup[heightmap[row][col]]

def generate_lookup():
    lookup = dict([(char, num+1) for num, char in enumerate('abcdefghijklmnopqrstuvwxyz')])
    # "Your current position (S) has elevation a, 
    # and the location that should get the best signal (E) has elevation z."
    lookup['S'] = 1     # elevation a
    lookup['E'] = 26    # elevation z
    return lookup

def get_index(char, heightmap):
    for row, elements in enumerate(heightmap):
        col  = [index for (index, item) in enumerate(elements) if item == char]
        if col != []:
            return (row, col[0])
        
def bfs(adjacency_list, start, end):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append((start, 0))

    while queue:
        node, dist = queue.popleft()
        row, col = node
        if node == end:
            return dist
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist+1))
    return -1

def part_one():
    filename = 'input.txt'

    heightmap = []
    with open(filename) as f:
        for line in f:
            l = list(line.strip())
            heightmap.append(l)
    
    height_lookup = generate_lookup()

    start = get_index('S', heightmap)
    end = get_index('E', heightmap)

    # adjacency list:
    # - coordinates/ID,
    # - reachable neighbors
    # - remove neighbors that are S or are too high up
    adjacency_list = dict()
    for row, lst in enumerate(heightmap):
        for col, node in enumerate(lst):
            pos = (row, col)
            neighbors = get_neighbors(heightmap, height_lookup, pos, start)
            adjacency_list[(row, col)] = neighbors

    shortest_dist = bfs(adjacency_list, start, end)
    print(shortest_dist)
    

if __name__ == "__main__":
    part_one()