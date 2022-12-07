class TreeNode:
    def __init__(self, inp):
        self.inp = inp
        self.leftChild = None
        self.rightChild = None


data = open('input.txt', 'r')
toRead = int(len(data.readlines()))
data.seek(0)
tree = {'/': {}}
commands = list()
for elem in range(0, toRead):
    line = data.readline().strip('\n').split(' ')
    print(line)
    if line[0] == '$':
        if line[1] == 'ls':
            tree[elem]

    elif line[0] == 'dir':
        tree[line[1]] = dict()

    else:
        tree[] = tuple(line)

print(commands)
