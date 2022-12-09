data = open('input.txt', 'r')

trees = []
for row, line in enumerate(data.readlines()):
    line = line.strip('\n')
    tre = list()
    for tree in line:
        tre.append(int(tree))
    trees.append(tre)

for i in range(0, len(trees)):
    print('%s ' % (trees[i]))

print(trees[-1][:])

num_visible = 0

# Loop through each tree in the grid.
for row in range(len(trees)):
    for col in range(len(trees[row])):
        # Check if the current tree is visible from the left.
        is_visible_left = True
        for i in range(col):
            if trees[row][i] >= trees[row][col]:
                is_visible_left = False
                break
        if is_visible_left:
            num_visible += 1
            continue
print(num_visible)