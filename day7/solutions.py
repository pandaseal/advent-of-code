# Find all of the directories with a total size of at most 100.000. What is the sum of the total sizes of those directories?
def part1():
    filesystem = {"/": {"files": [], "dirs": []}}
    # eg: filesystem = {"/": { 
    #                       "type": "dir",
    #                       "files": [18, 52], 
    #                       "dirs": ["a", "d"]
    #                       },
    #                   "/a/": {
    #                       "type": "dir",
    #                       "files": [],
    #                       "dirs": []
    #                   }

    # - / (dir)
    #   - a (dir)
    #       - e (dir)
    #           - i (file, size=584)
    #       - f (file, size=29116)
    #       - g (file, size=2557)
    #       - h.lst (file, size=62596)
    #   - b.txt (file, size=14848514)
    #   - c.dat (file, size=8504156)
    #   - d (dir)
    #       - j (file, size=4060174)
    #       - d.log (file, size=8033020)
    #       - d.ext (file, size=5626152)
    #       - k (file, size=7214296)

    path = [''] # current path
    print("filesystem:", filesystem)

    # read terminal input
    with open('ex-input.txt') as f:
        for line in f:
            l = line.strip().split()
            print(line.strip())

            if l[0] == '$': # command mode
                #print("command mode")

                if l[1] == 'cd': # change path
                    if l[2] == '..':
                        #print("old path:", path)
                        path = path[:-2]
                        #print("new path:", path)
                    elif l[2] == '/':
                        path = ['', '/']
                    else:                   
                        # check if dir in filesystem TODO B
                        # if it is, change path TODO A
                        #print("old path:", path)
                        path = path + [l[2], '/']
                        #print("new path:", path)

                        # if its not, raise error TODO C    
                #print("path:",path)       
            
            else: # list mode
                #print("list mode")

                if l[0] == 'dir': # dir
                    dir = l[1]
                    # check if dir in fileystem TODO B

                    # if not, add listed dir to filesystem TODO A
                    cwd_path = ''.join(path)
                    dir_path = cwd_path + dir + '/'
                    
                    filesystem[cwd_path]["dirs"].append(dir)
                    filesystem[dir_path] = {'files': [], 'dirs': []}

                    #print("add dir {} to path {}".format(l[1], cwd_path))

                else: # file
                    # check if file in filesystem yet TODO B
                    # if not, add file to filesystem TODO A
                    size = int(l[0])
                    cwd_path = ''.join(path)

                    filesystem[cwd_path]['files'].append(size)
                    #print("add file of size {} to path {}".format(size, cwd_path))
                
    print("final filesystem:", filesystem)

    # calculate sum of each directory
    for p in filesystem:
        print(p, recur_sum(filesystem, p))
                
    # sum all directories that have a size <= 100.000

def recur_sum(filesystem, dir):
    size = sum(filesystem[dir]['files'])
    if len(filesystem[dir]['dirs']) == 0:
        return size
    else:
        for child in filesystem[dir]['dirs']:
            return sum + recur_sum(filesystem, dir + child + '/')

if __name__ == "__main__":
    part1()