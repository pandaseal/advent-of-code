
# Find the item type that appears in both compartments of each rucksack. 
# What is the sum of the priorities of those item types?
def part1():

    # create lookup for priorities
    priority = get_priority_dict()
    sum = 0

    # read data
    with open('input.txt') as f:
        for line in f:
            # get content and size
            contents = list(line.strip())
            comp_size = int(len(contents)/2)
            
            # split compartments
            comp1 = contents[:comp_size]
            comp2 = contents[comp_size:]

            # find common item
            common = list(set(comp1).intersection(comp2))[0]

            # find priority of item + sum up
            sum += priority[common]

    print("Part 1:", sum)

# Find the item type that corresponds to the badges of each three-Elf group. 
# What is the sum of the priorities of those item types?
def part2():
    sum = 0
    priority = get_priority_dict()

    elfs = []

    # read data
    with open('input.txt') as f:
        for line in f:
            if len(elfs) < 2:
                # adds elf
                elfs.append(line.strip())
            elif len(elfs) == 2:
                # add third elf
                elfs.append(line.strip())

                # find common item
                common = list(set(elfs[0]).intersection(elfs[1]).intersection(elfs[2]))[0]

                # calculate its priority + add to sum
                sum += priority[common]

                # empty elfs list and start over
                elfs.clear()
            else:
                print("Something went wrong.")                   

    print("Part 2:", sum)

# create list of letters/items (source: https://datagy.io/python-list-alphabet/)
# then make a dict with corresponding priority of them
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def get_priority_dict():

    lower = [chr(value) for value in range(ord('a'), ord('a') + 26)]
    upper = [chr(value) for value in range(ord('A'), ord('A') + 26)]
    alphabet = lower + upper

    return dict(zip(alphabet, range(1, len(alphabet)+1)))


if __name__ == "__main__":
    #part1()
    part2()
