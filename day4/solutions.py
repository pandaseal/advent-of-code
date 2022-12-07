def part1(): # In how many assignment pairs does one range fully contain the other?
    overlapping = 0

    with open('input.txt') as f:
        for line in f:
            min1, max1, min2, max2 = get_minmax(line)

            if total_overlap(min1, max1, min2, max2):
                overlapping += 1

    print("Part 1:", overlapping)

def part2(): # In how many assignment pairs do the ranges overlap?
    overlapping = 0

    with open('input.txt') as f:
        for line in f:
            min1, max1, min2, max2 = get_minmax(line)

            if total_overlap(min1, max1, min2, max2) or some_overlap(min1, max1, min2, max2):
                overlapping += 1
    
    print("Part 2:", overlapping)

def get_minmax(line):
    assignments = line.strip().split(",")
    min1, max1 = [int(i) for i in assignments[0].split("-")]
    min2, max2 = [int(i) for i in assignments[1].split("-")]
    return min1, max1, min2, max2

def total_overlap(min1, max1, min2, max2):
    return (((min1 >= min2) and (max1 <= max2)) or ((min2 >= min1) and (max2 <= max1)))

def some_overlap(min1, max1, min2, max2):
    return (((max1 >= min2) and (max1 <= max2)) or ((min1 >= min2) and (min1 <= max2)))

if __name__ == "__main__":
    part1()
    part2()