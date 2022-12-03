data = open('input.txt', 'r')
## PART 1 ##
# sumOfPriorities = 0
# for rucksack in data.readlines():
#     rucksack = rucksack.strip('\n')
#     compartment_1 = rucksack[:(len(rucksack) // 2)]
#     compartment_2 = rucksack[(len(rucksack) // 2):]
#     priority = ''.join(set(compartment_1).intersection(compartment_2))
#     if priority.islower():
#         sumOfPriorities += (ord(priority) % 96)
#     elif priority.isupper():
#         sumOfPriorities += (ord(priority) - 38)
# print(sumOfPriorities)

## PART 2 ##

sumOfPrioritiesBadges = 0

for elem in range(0, 300, 3):
    line1 = data.readline().strip('\n')
    line2 = data.readline().strip('\n')
    line3 = data.readline().strip('\n')
    badge = ''.join(set(line1).intersection(line2).intersection(line3))
    if badge.islower():
        sumOfPrioritiesBadges += (ord(badge) % 96)
    elif badge.isupper():
        sumOfPrioritiesBadges += (ord(badge) - 38)
#    print(badge, ord(badge))
print(sumOfPrioritiesBadges)
