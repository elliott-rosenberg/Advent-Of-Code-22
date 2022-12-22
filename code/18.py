def process(file):
    lines = [l.strip().split(',') for l in open(file).readlines()]
    newLines = []
    xMax = 0
    yMax = 0
    zMax = 0
    for line in lines:
        line = [int(l) for l in line]
        newLines.append(line)
        if line[0] > xMax:
            xMax = line[0]
        if line[1] > yMax:
            yMax = line[1]
        if line[2] > zMax:
            zMax = line[2]
    bounds = [xMax, yMax, zMax]

    # print(newLines)
    return newLines, bounds


def printGrid(grid):
    for count, l in enumerate(grid):
        print(f"level: {count + 1}")
        for x in l:
            print(x)


def getExposedSides(coord, coordinates):
    x = coord[0]
    y = coord[1]
    z = coord[2]
    exposed = 6

    
    #covers direct adjacents
    if [x-1, y, z] in coordinates: #next to in x
        exposed -= 1
    if [x+1, y, z] in coordinates: #next to in x
        exposed -= 1
    if [x, y-1, z] in coordinates: #next to in y
        exposed -= 1
    if [x, y+1, z] in coordinates: #next to in y
        exposed -= 1
    if [x, y, z-1] in coordinates: #next to in z
        exposed -= 1
    if [x, y, z+1] in coordinates: #next to in z
        exposed -= 1
    return exposed


def getEnveloped(grid, bounds):
    # x = coord[0]
    # y = coord[1]
    # z = coord[2]

    xBound = bounds[0]
    yBound = bounds[1]
    zBound = bounds[2]
    internal = 0
    # valid = False
    for zCount, level in enumerate(grid):
        for yCount, row in enumerate(level):
            for xCount, spot in enumerate(row):
                # print(f"{xCount}, {yCount}, {zCount}")
                # print(f"{xBound}, {yBound}, {zBound}")
                # print(f"val: {grid[zCount][yCount][xCount]} ")
                # print(f"xPre: {grid[zCount][yCount][:xCount+1]} ")
                # print(f"xPost: {grid[zCount][yCount][xCount:]} ")

                if grid[zCount][yCount][xCount] == '.':
                    if ('#' in grid[zCount][yCount][:xCount]) and ('#' in grid[zCount][yCount][xCount:]): #is boxed in on the row
                        # print('reached x bounded')
                        v1 = False
                        v2 = False
                        for why in range(yBound):
                            # print(f"y check: value of spot: {grid[zCount][why][xCount]}")
                            if why < yCount and grid[zCount][why][xCount] == '#':
                                # print("reached v1")
                                v1 = True
                            if why >= yCount and grid[zCount][why][xCount] == '#':
                                # print("reached v2")
                                v2 = True
                                break
                        if v1 and v2: #contained in the y direction
                            # print(zBound)
                            # print(xCount, yCount, )
                            # print(grid[1][1][4])
                            # print(grid[2][1][4])
                            # print(grid[3][1][4])
                            # print(grid[4][1][4])
                            # print(grid[5][1][4])

                            v3 = False
                            v4 = False
                            for zee in range(zBound):
                                # print(f"z check: value of spot: {grid[zee][yCount][xCount]}")
                                if zee < zCount and grid[zee][yCount][xCount] == '#':
                                    # print("reached v3")
                                    v3 = True
                                if zee >= zCount and grid[zee][yCount][xCount] == '#':
                                    # print("reached v4")
                                    v4 = True
                                    break
                            if v3 and v4:
                                # print(xCount, yCount, zCount)
                                internal += 1
                            # if ('#' in grid[zCount][:yCount][xCount]) and ('#' in grid[zCount][yCount:][xCount]): #boxed in on y
                                # if ('#' in grid[:zCount][yCount][xCount]) and ('#' in grid[zCount:][yCount][xCount]):
                                #     print(xCount, yCount, zCount)
                                #     internal += 1

    return internal



# def getExternal(grid, bounds, surfaceArea):
#     # x = coord[0]
#     # y = coord[1]
#     # z = coord[2]

#     xBound = bounds[0]
#     yBound = bounds[1]
#     zBound = bounds[2]
#     internal = 0

#     SA = surfaceArea

#     # valid = False
#     for zCount, level in enumerate(grid):
#         for yCount, row in enumerate(level):
#             for xCount, spot in enumerate(row):
#                 # print(f"{xCount}, {yCount}, {zCount}")
#                 # print(f"{xBound}, {yBound}, {zBound}")
#                 # print(f"val: {grid[zCount][yCount][xCount]} ")
#                 # print(f"xPre: {grid[zCount][yCount][:xCount+1]} ")
#                 # print(f"xPost: {grid[zCount][yCount][xCount:]} ")

#                 if grid[zCount][yCount][xCount] == '#':
#                     if ('#' in grid[zCount][yCount][:xCount]):
#                         SA -= 1
#                     if ('#' in grid[zCount][yCount][xCount:]):
#                         SA -= 1
                    
                    
                    
                    
                    
                    
#                      and ('#' in grid[zCount][yCount][xCount:]): #is boxed in on the row
#                         # print('reached x bounded')
#                         v1 = False
#                         v2 = False
#                         for why in range(yBound):
#                             # print(f"y check: value of spot: {grid[zCount][why][xCount]}")
#                             if why < yCount and grid[zCount][why][xCount] == '#':
#                                 # print("reached v1")
#                                 v1 = True
#                             if why >= yCount and grid[zCount][why][xCount] == '#':
#                                 # print("reached v2")
#                                 v2 = True
#                                 break
#                         if v1 and v2: #contained in the y direction
#                             # print(zBound)
#                             # print(xCount, yCount, )
#                             # print(grid[1][1][4])
#                             # print(grid[2][1][4])
#                             # print(grid[3][1][4])
#                             # print(grid[4][1][4])
#                             # print(grid[5][1][4])

#                             v3 = False
#                             v4 = False
#                             for zee in range(zBound):
#                                 # print(f"z check: value of spot: {grid[zee][yCount][xCount]}")
#                                 if zee < zCount and grid[zee][yCount][xCount] == '#':
#                                     # print("reached v3")
#                                     v3 = True
#                                 if zee >= zCount and grid[zee][yCount][xCount] == '#':
#                                     # print("reached v4")
#                                     v4 = True
#                                     break
#                             if v3 and v4:
#                                 # print(xCount, yCount, zCount)
#                                 internal += 1
#                             # if ('#' in grid[zCount][:yCount][xCount]) and ('#' in grid[zCount][yCount:][xCount]): #boxed in on y
#                                 # if ('#' in grid[:zCount][yCount][xCount]) and ('#' in grid[zCount:][yCount][xCount]):
#                                 #     print(xCount, yCount, zCount)
#                                 #     internal += 1

#     return internal



def createGrid(coords, bounds):
    grid = []
    for z in range(bounds[2]):
        grid.append([['.']*bounds[0] for i in range(bounds[1])])
    surfaceArea = 0
    for coord in coords:
        grid[coord[2]-1][coord[1]-1][coord[0]-1] = '#'
        surfaceArea += getExposedSides(coord, coords)
    printGrid(grid)

    external = getExternal(grid, bounds, surfaceArea)
        
        


    #grid[z coord - 1][y coord - 1 (rows)][x coord - 1 (col)]
    #printGrid(grid)
    return surfaceArea, (external)


def solvePart1(coords, bounds):
    return createGrid(coords, bounds)



def solve(file):
    out = process(file)
    print(f"Part 1: {solvePart1(out[0], out[1])[0]}")
    print(f"Part 2: {solvePart1(out[0], out[1])[1]}")

solve("input/18/input1.txt")