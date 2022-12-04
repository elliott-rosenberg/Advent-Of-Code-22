from ast import Num
from string import ascii_lowercase
from string import ascii_uppercase
lines = [l.strip() for l in open("input/03/input1.txt").readlines()]
#part 1

count = 1
prio = {}
for c in ascii_lowercase:
    prio[c] = count 
    count += 1

for c in ascii_uppercase:
    prio[c] = count 
    count += 1

priorityCount = 0

# common_item = ''.join(
#     set(string1[0:len(string1)/2]).intersection(string1[len(string1)/2:-1])
# )


for line in lines:
    common_item = set(line[0:int(len(line)/2)]).intersection(line[int(len(line)/2):])
    priorityCount += prio[next(iter(common_item))]

#print(priorityCount)

#part2

lineCount = 0
lineArray = []
priorityCount = 0
for line in lines:
    lineCount += 1
    lineArray.append(line)
    if lineCount == 3:
        common_item1 = ''.join(
            set(lineArray[0]).intersection(lineArray[1])
            )
        common_item2 = ''.join(
            set(common_item1).intersection(lineArray[2])
            )
        priorityCount += prio[common_item2]
        lineCount = 0
        lineArray = []

print(priorityCount)


