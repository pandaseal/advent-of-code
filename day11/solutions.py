from collections import defaultdict

def main():

    monkeys = parse_monkeys('ex-input.txt')
    print(monkeys)

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