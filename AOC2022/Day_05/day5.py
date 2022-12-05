data = open('input.txt', 'r+')
data_2 = open('input.txt', 'r+')
cranes = [['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q'],  # 1
          ['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J'],  # 2
          ['F', 'B', 'H', 'W', 'P', 'M', 'Q'],  # 3
          ['V', 'S', 'T', 'D', 'F'],  # 4
          ['Q', 'L', 'D', 'W', 'V', 'F', 'Z'],  # 5
          ['Z', 'C', 'L', 'S'],  # 6
          ['Z', 'B', 'M', 'V', 'D', 'F'],  # 7
          ['T', 'J', 'B'],  # 8
          ['Q', 'N', 'B', 'G', 'L', 'S', 'P', 'H']  # 9
          ]

## PART 1 ##

# for elem in range(0, 501):
#     line = data.readline().strip('\n')
#     ops = line.split(' ', 5)
#     numOfCranes, fromStack, toStack = ops[1], ops[3], ops[5]
#     for i in range(0, int(numOfCranes)):
#         cranes[int(toStack) - 1].append(cranes[int(fromStack) - 1].pop())
#
# ch = ''
# for i in range(0, 9):
#     ch += ''.join(str(cranes[i][-1]))
# print(ch)

data.seek(0)
## PART 2 ##
for elem in range(0, 501):
    line = data.readline().strip('\n')
    ops = line.split(' ', 5)
    numOfCranes, fromStack, toStack = ops[1], ops[3], ops[5]
    for i in range(0, int(numOfCranes)):
        cranes[int(toStack) - 1].append(
            cranes[int(fromStack) - 1].pop(len(cranes[int(fromStack) - 1]) - (int(numOfCranes) - i)))

ans = ''
for i in range(0, 9):
    ans += ''.join(str(cranes[i][-1]))
print(ans)
