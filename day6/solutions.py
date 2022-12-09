from collections import deque

def unique(str):
    return (len(set(str)) == len(str))

def parse_n_search(length, filename='input.txt'):
    with open(filename) as f:
        message = deque(maxlen=length)
        i = 0

        while True:
            c = f.read(1)
            if not c:
                print("EOF")
                return -1
            
            message.append(c)
            i += 1
            
            if len(message) >= length:
                if unique(message):
                    return i

if __name__ == "__main__":
    print("Part 1:", parse_n_search(4))
    print("Part 2:", parse_n_search(14))