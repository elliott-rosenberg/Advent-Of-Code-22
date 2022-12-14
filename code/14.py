from logging import StreamHandler


def process(file):
    lines = [l.strip().split(' -> ') for l in open(file).readlines()]
    coords = []
    minX = 1000
    maxX = 0
    maxDepth = 0
    for line in lines:
        currPath = []
        for coord in line:
            coord = coord.split(',')
            coord = [int(n) for n in coord]
            if coord[0] < minX:
                minX = coord[0]
            if coord[0] > maxX:
                maxX = coord[0]
            if coord[1] > maxDepth:
                maxDepth = coord[1]
            currPath.append(coord)
        coords.append(currPath)
    adjustedCoords = []
    for lin in coords:
        lin = [[x[1], x[0] - minX + 1] for x in lin]
        adjustedCoords.append(lin)

    # print(adjustedCoords)
    maxX = maxX - minX + 1
    start = 500 - minX + 1

    # print(coords)
    # print(maxX)
    # print(maxDepth)
    # print(start)
    return [adjustedCoords, maxX, maxDepth, start]


def createSandMap(coords):
    sand = coords[0]
    maxBound = coords[1]
    maxDepth = coords[2]
    start = coords[3]

    # print(f"starting sand: {sand}")
    #build the sand box, dims from 0 to maxBound + 1 (allows for sand to hit the overflow spots)
    #overflow spots are (0,maxDepth), (maxBound + 2), maxDepth

    sandBox = [['.']*(maxBound + 2) for i in range(maxDepth+1)]
    sandBox[0][start] = '+'
    sandBox[maxDepth][0] = 'x'
    sandBox[maxDepth][maxBound + 1] = 'x'

    # print(f"maximum x val: {maxBound}, max depth: {maxDepth}, start: {start}")
    

    for s in sand:
        # print(f"sand path {s}")
        # print(len(s))
        for x in range(len(s)-1):
            # print(f"x: {x}")
            if s[x][0] == s[x+1][0]:
                # print(f"horizontal between {s[x]} and {s[x+1]}")
                #draw horizontal line
                higher = max(s[x][1], s[x+1][1])
                lower = min(s[x][1], s[x+1][1])
                for y in range(lower, higher+1):
                    sandBox[s[x][0]][y] = '#'
            elif s[x][1] == s[x+1][1]:
                # print(f"vertical between {s[x]} and {s[x+1]}")
                #draw vertical line
                higher = max(s[x][0], s[x+1][0])
                lower = min(s[x][0], s[x+1][0])
                for y in range(lower, higher+1):
                    sandBox[y][s[x][1]] = '#'
    # for s in sandBox:
    #     print(s)

    
                
    return sandBox

def pourSand(sandMap, coords):
    sandBox = sandMap
    startPos = coords[3]
    pellets = 0

    while True:
        pellets += 1
        restingPos = drop(sandBox, 0, startPos)
        if restingPos != [0,0]:
            sandBox[restingPos[0]][restingPos[1]] = 'o'
            # print(pellets)
            # for s in sandBox:
            #     print(s)
        else:
            return pellets-1
        


def drop(sandBox, startDepth, startX):
    # print(f"startDepth: {startDepth}, startX: {startX}")
    # print(f"sandBox bounds: {len(sandBox)}, {len(sandBox[0])}")
    if startDepth == len(sandBox) - 1:
        return ([0,0])
    # if sandBox[startDepth][startX] == 'x':#if overflow has been reached
    #     return([0,0])
    # elif startX > 0 and startDepth < len(sandBox)-1:
    #     if sandBox[startDepth+1][startX-1] == 'x':
    #         return([0,0])
    # elif startX < (len(sandBox[0])) and startDepth < len(sandBox)-1:
    #     if sandBox[startDepth+1][startX+1] == 'x':
    #         return([0,0])
    # elif startDepth < len(sandBox):
    #     if sandBox[startDepth+1][startX] == 'x':
    #         return([0,0])


    if sandBox[startDepth+1][startX] == '.': #if below is free, drop below
        # print("below free")
        return drop(sandBox, startDepth + 1, startX)
    elif sandBox[startDepth+1][startX] == '#' or sandBox[startDepth+1][startX] == 'o': #if below taken, but bottom left free, drop left
        if sandBox[startDepth+1][startX-1] == '.':
            # print("below left")
            return drop(sandBox, startDepth + 1, startX-1)#else drop right
        elif sandBox[startDepth+1][startX+1] == '.':
            # print("below right")
            return drop(sandBox, startDepth + 1, startX+1)
        else:
            # print(f"rested at depth {startDepth}, x: {startX}") 
            return([startDepth, startX])
    elif sandBox[startDepth+1][startX] == 'x':
        return ([0,0])
    # print(sandBox[startDepth+1][startX])
    raise Exception("shouldn't be here given input")

def createSandMap2(coords):
    sand = coords[0]
    cap = 150
    # print(sand)
    maxBound = coords[1]
    maxDepth = coords[2]
    start = coords[3]
    maxBound = maxBound + cap
    start = start + cap
    for c in sand: #adding cap to both sides for pyramid
        for path in c:
            path[1] += cap



    # print(f"starting sand: {sand}")
    #build the sand box, dims from 0 to maxBound + 1 (allows for sand to hit the overflow spots)
    #overflow spots are (0,maxDepth), (maxBound + 2), maxDepth

    sandBox = [['.']*(maxBound + 2 + cap) for i in range(maxDepth+3)]
    sandBox[0][start] = '+'
    for s in range(len(sandBox[maxDepth+2])):
        sandBox[maxDepth+2][s] = '#'

    for s in sand:
        # print(f"sand path {s}")
        # print(len(s))
        for x in range(len(s)-1):
            # print(f"x: {x}")
            if s[x][0] == s[x+1][0]:
                # print(f"horizontal between {s[x]} and {s[x+1]}")
                #draw horizontal line
                higher = max(s[x][1], s[x+1][1])
                lower = min(s[x][1], s[x+1][1])
                for y in range(lower, higher+1):
                    sandBox[s[x][0]][y] = '#'
            elif s[x][1] == s[x+1][1]:
                # print(f"vertical between {s[x]} and {s[x+1]}")
                #draw vertical line
                higher = max(s[x][0], s[x+1][0])
                lower = min(s[x][0], s[x+1][0])
                for y in range(lower, higher+1):
                    sandBox[y][s[x][1]] = '#'
    # for s in sandBox:
    #     print(s)
    return sandBox
    # print(f"maximum x val: {maxBound}, max depth: {maxDepth}, start: {start}")
    


def pourSand2(sandMap, coords):
    cap = 150
    sandBox = sandMap
    startPos = coords[3] + cap
    pellets = 0

    while True:
        pellets += 1
        restingPos = drop2(sandBox, 0, startPos)
        if restingPos != [0,startPos]:
            sandBox[restingPos[0]][restingPos[1]] = 'o'
            # print(pellets)
            # for s in sandBox:
            #     print(s)
        else:
            return pellets

def drop2(sandBox, startDepth, startX):

    if sandBox[startDepth+1][startX] == '.': #if below is free, drop below
        # print("below free")
        return drop2(sandBox, startDepth + 1, startX)
    elif sandBox[startDepth+1][startX] == '#' or sandBox[startDepth+1][startX] == 'o': #if below taken, but bottom left free, drop left
        if sandBox[startDepth+1][startX-1] == '.':
            # print("below left")
            return drop2(sandBox, startDepth + 1, startX-1)#else drop right
        elif sandBox[startDepth+1][startX+1] == '.':
            # print("below right")
            return drop2(sandBox, startDepth + 1, startX+1)
        else:
            # print(f"rested at depth {startDepth}, x: {startX}") 
            return([startDepth, startX])
    # print(sandBox[startDepth+1][startX])
    raise Exception("shouldn't be here given input")

def solvePart1(coords):
    sandMap = createSandMap(coords)
    pellets = pourSand(sandMap, coords)
    return pellets

def solvePart2(coords):
    sandMap = createSandMap2(coords)
    pellets = pourSand2(sandMap, coords)
    return pellets


def solve(file):
    print(f"Part 1: {solvePart1(process(file))}")
    print(f"Part 2: {solvePart2(process(file))}")

solve("input/14/input1.txt")