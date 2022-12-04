data = open('input.txt', 'r')

fullyContainCounter = 0
overlapCounter = 0
for line in data.readlines():
    line = line.strip('\n')
    firstElf, secondElf = line.split(',')
    firstElf = firstElf.split('-')
    secondElf = secondElf.split('-')
    # PART 1
    # if int(firstElf[0]) <= int(secondElf[0]) and int(firstElf[1]) >= int(secondElf[1]):
    #     fullyContainCounter += 1
    #
    # elif int(secondElf[0]) <= int(firstElf[0]) and int(secondElf[1]) >= int(firstElf[1]):
    #     fullyContainCounter += 1

    # PART 2
    if int(firstElf[0]) <= int(secondElf[0]) <= int(firstElf[1]):
        overlapCounter += 1
    elif int(firstElf[0]) <= int(secondElf[1]) <= int(firstElf[1]):
        overlapCounter += 1
    elif int(secondElf[0]) <= int(firstElf[0]) <= int(secondElf[1]):
        overlapCounter += 1
    elif int(secondElf[0]) <= int(firstElf[1]) <= int(secondElf[1]):
        overlapCounter += 1
print(fullyContainCounter)
print(overlapCounter)
