lines = [l.strip() for l in open("input/01/input1.txt").readlines()]

#part 1
maxCals = 0
tempTotal = 0

for line in lines:
    if line == '':
        if tempTotal > maxCals:
            maxCals = tempTotal
        tempTotal = 0
    else: 
        line = int(line)
        tempTotal += line
print(maxCals)

#part2

calsList = []
for line in lines:
    if line == '':
        calsList.append(tempTotal)
        tempTotal = 0
    else: 
        line = int(line)
        tempTotal += line

calsList = sorted(calsList, reverse=True)
print(calsList)
print(calsList[1] + calsList[2] + calsList[3])



    


