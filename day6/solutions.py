from collections import deque

def part1():
    length = 4
    with open('input.txt') as f:
        marker = deque(maxlen=length)
        i = 0

        while True:
            c = f.read(1)
            if not c:
                print("EOF")
                break
            
            marker.append(c)
            i += 1
            
            if len(marker) >= length:
                if unique(marker):
                    print("Part 1:", i)
                    break

def part2():
    length = 14
    with open('input.txt') as f:
        message = deque(maxlen=length)
        i = 0

        while True:
            c = f.read(1)
            if not c:
                print("EOF")
                break
            
            message.append(c)
            i += 1
            
            if len(message) >= length:
                if unique(message):
                    print("Part 2:", i)
                    break

def unique(str):
    if(len(set(str)) == len(str)):
        return True
    return False

if __name__ == "__main__":
    #part1()
    part2()
