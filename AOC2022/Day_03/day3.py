
data = open('input.txt', 'r')
sumOfPriorities = 0
for rucksack in data.readlines():
    rucksack = rucksack.strip('\n')
    compartment_1 = rucksack[:(len(rucksack) // 2)]
    compartment_2 = rucksack[(len(rucksack) // 2):]
    priority = ''.join(set(compartment_1).intersection(compartment_2))
    if priority.islower():
        sumOfPriorities += (ord(priority) % 96)
    elif priority.isupper():
        sumOfPriorities += (ord(priority) - 38)
print(sumOfPriorities)
