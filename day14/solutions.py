from collections import defaultdict

def parse_paths(filename="input.txt") -> list:
    with open(filename) as f:
        return [[
                [int(n) for n in coord.split(",")]
                    for coord in path.split(" -> ")
            ] 
                for path in f.read().split("\n")
        ]
    
def print_grid(graph):
    min_x = min(graph.keys())
    max_x = max(graph.keys())
    min_y = min(graph[min_x].keys())
    max_y = max(graph[min_x].keys())
    for y in range(0, 3):
        row = '  '
        for x in range(min_x, max_x+1):
            row += str(x)[y] + ' '
        print(row)

    for y in range(min_y, max_y+1):
        row = str(y) + ' '
        for x in range(min_x, max_x+1):
            row += graph[x][y] + ' '
        print(row)

def get_dimensions(paths) -> list:
    min_x = 10000000000
    min_y = 0 # ! special case
    max_x, max_y = 0, 0
    for path in paths:
        for [x, y] in path:
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
    return [min_x, max_x, min_y, max_y]

def get_start_graph(paths) -> defaultdict:
    [min_x, max_x, min_y, max_y] = get_dimensions(paths)
    graph = defaultdict(defaultdict)
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            graph[x][y] = '.'

    for path in paths:
        for i in range(len(path)-1):
            [start_x, start_y] = path[i]
            [end_x, end_y] = path[i+1]
            if start_x == end_x:
                fr = min([start_y, end_y])
                to = max([start_y, end_y])
                for y in range(fr, to+1):
                    graph[start_x][y] = '#'
            elif start_y == end_y:
                fr = min([start_x, end_x])
                to = max([start_x, end_x])
                for x in range(fr, to+1):
                    graph[x][start_y] = '#'
    return graph

def within_bounds(coord, dimensions) -> bool:
    [min_x, max_x, min_y, max_y] = dimensions
    return min_x <= coord[0] <= max_x and min_y <= coord[1] <= max_y

if __name__ == "__main__":
    paths = parse_paths("input.txt")
    dimensions = get_dimensions(paths)
    graph = get_start_graph(paths)
    sand = [500, 0]
    graph[sand[0]][sand[1]] = '+'

    overflow = False
    counter = 0
    
    while not overflow:
        current = sand
        at_rest = False
        while not at_rest:
            down = [current[0], current[1]+1]
            if within_bounds(down, dimensions):
                match graph[down[0]][down[1]]:
                    case '#' | 'o':
                        left = [current[0]-1, current[1]+1]
                        if within_bounds(left, dimensions):
                            match graph[left[0]][left[1]]:
                                case '#' | 'o':
                                    right = [current[0]+1, current[1]+1]
                                    if within_bounds(right, dimensions):
                                        match graph[right[0]][right[1]]:
                                            case '#' | 'o':
                                                at_rest = True
                                                counter += 1
                                                graph[current[0]][current[1]] = 'o'
                                            case '.':
                                                current = right
                                    overflow = True
                                    break
                                case '.':
                                    current = left
                        overflow = True
                        break
                    case '.':
                        current = down
            overflow = True
            break

    print_grid(graph)
    print("part 1:", counter)     
    

