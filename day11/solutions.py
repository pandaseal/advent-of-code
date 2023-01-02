from collections import defaultdict
from heapq import nlargest

ITEMS, OP, NUM, DIV, A, B = range(6)

def main():

    monkeys = parse_monkeys('input.txt')

    #part1(monkeys)
    part2(monkeys)

def part1(monkeys):
    inspected_items = stuff_slinging_shenanigans(20, monkeys, False)
    print("Part1:", monkey_business(inspected_items))

def part2(monkeys):
    inspected_items = stuff_slinging_shenanigans(20, monkeys, True) # TODO this is too slow!
    print("Part 2:", monkey_business(inspected_items))

def stuff_slinging_shenanigans(rounds, monkeys, anxious):
    inspected_items = defaultdict(int)

    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkeys[monkey][ITEMS]:
                worry_level = operation(item, monkeys[monkey][OP], monkeys[monkey][NUM])
                if not anxious:
                    worry_level = int(worry_level/3)
                
                if worry_level % monkeys[monkey][DIV] == 0:
                    throw_to = monkeys[monkey][A]
                else:
                    throw_to = monkeys[monkey][B]
                monkeys[throw_to][ITEMS].append(worry_level)

                inspected_items[monkey] += 1

            monkeys[monkey][ITEMS] = []

    return inspected_items

#def faster_solve():
#    return inspected_items


def monkey_business(inspected_items):
    most_active = nlargest(2, list(inspected_items.values()))
    return most_active[0]*most_active[1]

def operation(worry_level, operator, number):
    match operator:
        case '+':
            return int(worry_level + number)
        case '*':
            return int(worry_level * number)
        case '**':
            return int(worry_level ** 2)
    return -1

def parse_monkeys(filename):

    monkeys = {}
    monkey_nr = -1

    with open(filename) as f:
        for line in f:
            l = line.strip().split()

            match l:
                case []:
                    monkey_nr = -1
                case 'Monkey', _:
                    monkey_nr = int(l[1][0])
                    monkeys[monkey_nr] = {}
                case 'Starting', *_:
                    monkeys[monkey_nr][ITEMS] = [int(i.replace(',', '')) for i in l[2:]] 
                case 'Operation:', _, _, _, _, 'old':
                    monkeys[monkey_nr][OP] = '**'
                    monkeys[monkey_nr][NUM] = 2
                case 'Operation:', _, _, _, operator, number:
                    monkeys[monkey_nr][OP] = operator
                    monkeys[monkey_nr][NUM] = int(number)
                case 'Test:', *_:
                    monkeys[monkey_nr][DIV] = int(l[-1])
                case 'If', 'true:', *_:
                    monkeys[monkey_nr][A] = int(l[-1])
                case 'If', 'false:', *_:
                    monkeys[monkey_nr][B] = int(l[-1])
                case _: 
                    print("EXITING! Error while parsing:", l)
                    exit()
    return monkeys


if __name__ == "__main__":
    main()