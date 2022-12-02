lines = [l.strip() for l in open("input/02/input1.txt").readlines()]
#part 1

totalScore = 0
for line in lines:
    if (line[0] == 'A'):
        if (line[2] == 'X'):
            totalScore +=4
            
        elif (line[2] == 'Y'):
            totalScore +=8


        elif (line[2] == 'Z'):
            totalScore +=3
    
    if (line[0] == 'B'):
        if (line[2] == 'X'):
            totalScore +=1
            
        elif (line[2] == 'Y'):
            totalScore +=5

        elif (line[2] == 'Z'):
            totalScore +=9

    if (line[0] == 'C'):
        if (line[2] == 'X'):
            totalScore +=7
            
        elif (line[2] == 'Y'):
            totalScore +=2

        elif (line[2] == 'Z'):
            totalScore +=6


#part 2

totalScore = 0
for line in lines:
    if (line[0] == 'A'):
        if (line[2] == 'X'):
            totalScore +=3
            
        elif (line[2] == 'Y'):
            totalScore +=4


        elif (line[2] == 'Z'):
            totalScore +=8
    
    if (line[0] == 'B'):
        if (line[2] == 'X'):
            totalScore +=1
            
        elif (line[2] == 'Y'):
            totalScore +=5

        elif (line[2] == 'Z'):
            totalScore +=9

    if (line[0] == 'C'):
        if (line[2] == 'X'):
            totalScore +=2
            
        elif (line[2] == 'Y'):
            totalScore +=6

        elif (line[2] == 'Z'):
            totalScore +=7
print(totalScore)


    
