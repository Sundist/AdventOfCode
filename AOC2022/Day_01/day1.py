# Total 242 Elves
data = open('input.txt', 'r')
caloriesList = list()
caloriesSum = 0
index = 0
for i in data.readlines():
    print(i)
    if i == '\n':
        caloriesSum = 0
        index += 1
    else:
        caloriesSum += int(i)
        caloriesList.insert(index, caloriesSum)

print(max(caloriesList))
print(len(caloriesList))
print(caloriesList)
# PART_2
# Find top three most carrying Elves and sum of them
sumOfThree = 0
for i in range(3):
    sumOfThree += max(caloriesList)
    caloriesList.remove(max(caloriesList))
print(sumOfThree)
