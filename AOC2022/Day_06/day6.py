with open('input.txt', 'r') as data:
    data_stream = data.read().strip('\n')

## PART 1 ##
# i = 0
# marker = ''  # 4 chars
# while len(set(marker)) != 4 and i < len(data_stream):
#     marker = ''.join(data_stream[i:i + 4])
#     if len(set(marker)) == 4:
#         print(marker, data_stream[i:i + 4], set(marker), i, i + 4)
#     i += 1

## PART 2 ##

i = 0
marker = ''  # 14 chars
while len(set(marker)) != 14 and i < len(data_stream):
    marker = ''.join(data_stream[i:i + 14])
    if len(set(marker)) == 14:
        print(marker, data_stream[i:i + 14], set(marker), i, i + 14)
    i += 1
