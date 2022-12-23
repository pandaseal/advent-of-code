from collections import defaultdict
from heapq import nlargest

def main():

    monkeys = parse_monkeys('input.txt')

    monkeys, inspected_items = stuff_slinging_shenanigans(20, monkeys)

    print(monkey_business(inspected_items))


def stuff_slinging_shenanigans(rounds, monkeys):
    inspected_items = defaultdict(int)

    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkeys[monkey]['items']:
                worry_level = operation(item, monkeys[monkey]['operator'], monkeys[monkey]['number'])
                worry_level = int(worry_level/3)
                
                if worry_level % monkeys[monkey]['divider'] == 0:
                    throw_to = monkeys[monkey]['true']
                else:
                    throw_to = monkeys[monkey]['false']
                monkeys[throw_to]['items'].append(worry_level)

                inspected_items[monkey] += 1

            monkeys[monkey]['items'] = []

    return monkeys, inspected_items

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
                    monkeys[monkey_nr]['items'] = [int(i.replace(',', '')) for i in l[2:]] 
                case 'Operation:', _, _, _, _, 'old':
                    monkeys[monkey_nr]['operator'] = '**'
                    monkeys[monkey_nr]['number'] = 2
                case 'Operation:', _, _, _, operator, number:
                    monkeys[monkey_nr]['operator'] = operator
                    monkeys[monkey_nr]['number'] = int(number)
                case 'Test:', *_:
                    monkeys[monkey_nr]['divider'] = int(l[-1])
                case 'If', 'true:', *_:
                    monkeys[monkey_nr]['true'] = int(l[-1])
                case 'If', 'false:', *_:
                    monkeys[monkey_nr]['false'] = int(l[-1])
                case _: 
                    print("EXITING! Error while parsing:", l)
                    exit()
    return monkeys


if __name__ == "__main__":
    main()