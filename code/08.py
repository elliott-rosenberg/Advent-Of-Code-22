
def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    tMap = []
    for row in rows:
        rowNums = [int(x) for x in row]
        tMap.append(rowNums)
    return tMap


def solvePart1(tMap):
    return getVisible(tMap)

def solvePart2(tMap):
    return getSurroundings(tMap)



def getSurroundings(tMap):
    maxScore = 0
    for i in range(len(tMap)):
        for j in range(len(tMap[i])):
            preRow = tMap[i][:j]
            postRow = tMap[i][j+1:]
                
            col = []
            for x in range(len(tMap)):
                col.append(tMap[x][j])

                
            preCol = col[:i]
            postCol = col[i+1:]
            surroundings = [preRow, postRow, preCol, postCol]
            score = getScenicScore(surroundings, tMap[i][j])
            if score > maxScore:
                maxScore = score



    return maxScore


def getScenicScore(surroundings, curr):
    score = []
    for count, di in enumerate(surroundings):
        if len(di) == 1:
            score.append(1)
        else:
            dirScore = 0
            for x in range(len(di)):
                tree = di.pop((count %2)-1) #pops the last for 0 and 2, first for 1 and 3
                dirScore += 1
                if tree >= curr:
                    break
            score.append(dirScore)
    result = 1
    for x in score:
        result = result * x
    return result

            







def getVisible(tMap):
    visible = 0
    for i in range(len(tMap)):
        for j in range(len(tMap[i])):
            if (i == 0 or tMap[i] == tMap[-1] or j ==0 or (j == len(tMap[0])-1)): #is around the edges
                visible += 1
            else:
                preRow = tMap[i][:j]
                postRow = tMap[i][j+1:]
                
                col = []
                for x in range(len(tMap)):
                    col.append(tMap[x][j])

                
                preCol = col[:i]
                postCol = col[i+1:]
                # print(f"{tMap[i][j], i, j } number")
                # print(preRow, postRow, preCol, postCol)
                # print(col)

                
                if ((all(tMap[i][j] > y for y in (preRow))) or (all(tMap[i][j] > y for y in (postRow))) or 
                (all(tMap[i][j] > y for y in (preCol))) or (all(tMap[i][j] > y for y in (postCol)))):
                    
                    visible += 1


    return visible

def solve(file):
    treeMap = process(file)
    print(f"Part 1: {solvePart1(treeMap)}")
    print(f"Part 2: {solvePart2(treeMap)}")

solve("input/08/input1.txt")