from collections import deque 
from math import prod, lcm

ITEMS, OP, NUM, DIV, A, B = range(6)

def part1():
    monkeys = parse_monkeys('input.txt')
    inspected_items = stuff_slinging_shenanigans(20, monkeys, False)
    print("Part 1:", monkey_business(inspected_items))

def part2():
    monkeys = parse_monkeys('input.txt')
    inspected_items = stuff_slinging_shenanigans(10_000, monkeys, True)
    print("Part 2:", monkey_business(inspected_items))

def stuff_slinging_shenanigans(rounds, monkeys, anxious):
    inspected_items = [0] * len(monkeys)

    for _ in range(rounds):
        for i, m in enumerate(monkeys):
            while m[ITEMS]:
                inspected_items[i] += 1
                worry_level = operation(m[ITEMS].popleft(), m[OP], m[NUM])

                if not anxious:
                    worry_level = int(worry_level/3)
                else:
                    # genious solution by: https://github.com/viliampucik/adventofcode/blob/master/2022/11.py
                    worry_level %= lcm(*(m[DIV] for m in monkeys))

                if worry_level % m[DIV] == 0:
                    monkeys[m[A]][ITEMS].append(worry_level)
                else:
                    monkeys[m[B]][ITEMS].append(worry_level)

    return inspected_items

def monkey_business(inspected_items):
    return prod(sorted(inspected_items)[-2:])

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

    monkeys = []

    with open(filename) as f:
        for line in f:
            l = line.strip().split()

            match l:
                case []:
                    continue
                case 'Monkey', _:
                    monkey_nr = int(l[1][0])
                case 'Starting', *_:
                    items = deque([int(i.replace(',', '')) for i in l[2:]])
                    monkeys.append([items, str, int, int, int, int])
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
    part1()
    part2()