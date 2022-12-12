from string import ascii_lowercase
from wsgiref.validate import ErrorWrapper

def process(file):
    prio = {}
    for count, c in enumerate(ascii_lowercase):
        prio[c] = count+1 

    lines = [list(l.strip()) for l in open(file).readlines()]
    SRow = 0
    SCol = 0
    ERow = 0
    ECol = 0

    newLines = lines

    for line in lines:
        for colCount, x in enumerate(line):
            if x == 'S':
                newLines[lines.index(line)][colCount] = 1
                SRow = lines.index(line)
                SCol = colCount
            elif x == 'E':
                newLines[lines.index(line)][colCount] = 26
                ERow = lines.index(line)
                ECol = colCount
            else: 
                newLines[lines.index(line)][colCount] = prio[x]

    rows = len(lines)
    cols = len(lines[0])

    return [newLines, [SRow, SCol], [ERow, ECol], [rows, cols]]


def populateGrid(info):
    grid = info[0]
    # for x in grid:
    #     print(x)
    starting = info[1]
    ending = info[2]
    bounds = info[3]
    # print(bounds)
    # i = [-1, 1, 0, 0]
    # j = [0,0,-1, 1]
    zipped = [(-1,0), (1,0), (0,-1), (0,1)]

    minSteps = [ [100000000]*bounds[1] for i in range(bounds[0])]#make empty minSteps Array
    minSteps[ending[0]][ending[1]] = 0
    nextBox = [ending]

    while len(nextBox) != 0:
        # print(f"start of loop: {nextBox}")
        nextIn = nextBox[0]
        # print(f"next In: {nextIn}")
        for i, j in zipped:
            # print(i,j)
            # print("next row, next col")
            # print(nextIn[0]+i)
            # print((nextIn[1]+j))
            
            if (((nextIn[0]+i) >= 0) and ((nextIn[0]+i) < bounds[0]) and ((nextIn[1]+j) >= 0) and ((nextIn[1]+j) < bounds[1])):
                # print(f"currNextInVal {grid[nextIn[0]][nextIn[1]]}")
                # print(f"currChecking {grid[nextIn[0]+i][nextIn[1]+j]}")
                if (grid[nextIn[0]][nextIn[1]] - grid[nextIn[0]+i][nextIn[1]+j] <= 1): # or (grid[nextIn[0]][nextIn[1]] - grid[nextIn[0]+i][nextIn[1]+j] == 0)check if next box is one higher or equal to currBox
                    # print('reached1')
                    # print(minSteps[nextIn[0]][nextIn[1]] + 1)
                    # print(minSteps[nextIn[0]+i][nextIn[1]+j])
                    if (minSteps[nextIn[0]][nextIn[1]] + 1) < minSteps[nextIn[0]+i][nextIn[1]+j]: # or minSteps[nextIn[0]+i][nextIn[1]+j] == '.' if next box is empty or hasn't been filled with a better number
                        # print('reached2')
                        minSteps[nextIn[0]+i][nextIn[1]+j] = minSteps[nextIn[0]][nextIn[1]] + 1 #next boxes around the box are filled with one more
                        nextBox.append([nextIn[0]+i,nextIn[1]+j])
                        # print(nextBox)

        nextBox.pop(0)
        # print(nextBox)
    # for y in minSteps:
    #     print(y)
    
    return (minSteps[starting[0]][starting[1]])


    


def solvePart1(file):
    return populateGrid(file)

def solvePart2(file):
    return True


def solve(file):
    info = process(file)
    print(f"Part 1: {solvePart1(info)}")
    print(f"Part 2: {solvePart2(info)}")

solve("input/12/input1.txt")