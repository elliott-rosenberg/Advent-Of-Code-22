lines = [l.strip() for l in open("input/04/input1.txt").readlines()]




#part 1
count = 0
for line in lines:
    sections = line.split(',')
    bounds = [l.split('-') for l in sections]
    if (int(bounds[0][0]) >= int(bounds[1][0])) and (int(bounds[0][-1]) <= int(bounds[1][-1])):
        count += 1
    elif (int(bounds[0][0]) <= int(bounds[1][0])) and (int(bounds[0][-1]) >= int(bounds[1][-1])):
        count += 1
print(count)

#part 2
count = 0
for line in lines:
    sections = line.split(',')
    bounds = [l.split('-') for l in sections]
    if (int(bounds[0][0]) <= int(bounds[1][0])) and (int(bounds[0][-1]) >= int(bounds[1][-1])):
        count += 1
    elif (int(bounds[0][0]) <= int(bounds[1][-1])) and (int(bounds[0][-1]) >= int(bounds[1][-1])):
        count += 1
    elif (int(bounds[1][0]) <= int(bounds[0][0])) and (int(bounds[1][-1]) >= int(bounds[0][0])):
        count += 1
    elif (int(bounds[1][0]) <= int(bounds[0][-1])) and (int(bounds[1][-1]) >= int(bounds[0][-1])):
        count += 1

print(count)