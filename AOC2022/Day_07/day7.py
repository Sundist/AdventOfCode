import string

data = open('input.txt', 'r')
toRead = int(len(data.readlines()))
data.seek(0)
tree = {}
child = ''
byteSize = 0
size = list()
parent = ''

for i in range(toRead):
    line = data.readline().strip('\n').split(' ')
    if line[0] == '$' and line[1] == 'cd':
        if line[2] != '..':
            parent = line[2]
            tree[parent] = []

        else:
            parent = child

    elif line[0] == '$' and line[1] == 'ls':
        print('ls')

    else:
        tree[parent].append(tuple(line))
        if tuple(line)[0] != 'dir':
            if int(tuple(line)[0]) < 100000:
                size.append(int(tuple(line)[0]))

# for elem in range(0, toRead):
#     line = data.readline().strip('\n').split(' ')
#     if line[0] == '$':
#         if line[1] == 'cd' and line[2] != '..':
#             parent = line[2]
#             child = line[2]
#             tree[parent] = []
#         elif line[2] == '..':
#             child = parent
#         else:
#             continue
#     elif line[0] != '$':
#         tree[parent].append(tuple(line))
#         if line[0] != 'dir':
#             size.append(int(line[0]))
#         # tree[???].append(line[2])
#
# for i in tree.keys():
#     print("%s:\t\t%s" % (i, tree[i]))
#
# print(size)
# print(len(size))
#
