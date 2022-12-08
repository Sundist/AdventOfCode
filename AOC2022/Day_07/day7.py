import string

data = open('input.txt', 'r')
toRead = int(len(data.readlines()))
data.seek(0)
tree = {}
dirs = ''
byteSize = 0
size = list()

for elem in range(0, toRead):
    line = data.readline().strip('\n').split(' ')
    if line[0] == '$':
        if line[1] == 'cd' and line[2] != '..':
            dirs = line[2]
            tree[dirs] = []
        elif line[1] == 'ls':
            continue
    elif line[0] != '$':
        tree[dirs].append(tuple(line))
        if line[0] != 'dir':
            size.append(int(line[0]))
        # tree[???].append(line[2])

for i in tree.keys():
    print("%s:\t\t%s" % (i, tree[i]))

print(size)
print(len(size))
print(set(size))
print(len(set(size)))