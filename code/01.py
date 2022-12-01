lines = [l.strip() for l in open("input/01/input1.txt").readlines()]
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

    


