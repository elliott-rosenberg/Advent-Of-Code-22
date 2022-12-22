#defining static vars
AIR = '.'
ROCK = '#'
FLOOR = '_'
CHAMBER_WIDTH = 7
START_POS = 0, 2
LEFT = '<'
RIGHT = '>'


def isEmpty(chamber, r, c):
   # print(f"row: {r}, col: {c}, result: {r >= 0 and r < len(chamber) and c >= 0 and c < CHAMBER_WIDTH and chamber[r][c] == AIR}")
    return r >= 0 and r < len(chamber) and c >= 0 and c < CHAMBER_WIDTH and chamber[r][c] == AIR
        

def getEmpties(chamber):
    empties = 0
    for row in chamber:
        if row == ['.','.','.','.','.','.', '.']:
            empties += 1
        else:
            return empties

    

class MinusRock:
    def __init__(self, chamber):
        self.chamber = chamber
        self.currRow, self.currCol = START_POS
        self.height = 1
    
    def printData(self):
        print(f"topRow: {self.currRow}, chamberLength: {len(self.chamber)}")
        print(f"rockHeight = {len(self.chamber)-self.currRow-1}")


    def add(self, char):
        for i in range(self.currCol, self.currCol+4):
            self.chamber[self.currRow][i] = char
        if char == '#':
            empties = getEmpties(self.chamber)
            if empties <= 3 + 3:
                for i in range(3 + 3 - empties):
                    self.chamber.insert(0, ['.','.','.','.','.','.', '.'])
            else:
                for i in range(abs(3 + 3 - empties)):
                    if self.chamber[0] == ['.','.','.','.','.','.', '.']:
                        self.chamber.pop(0)


    def moveLeft(self):
        if not isEmpty(self.chamber, self.currRow, self.currCol-1):
            return False
        else: 
            self.currCol -= 1
            return True

    def moveRight(self):
        if not isEmpty(self.chamber, self.currRow, self.currCol+4):
            return False
        else: 
            self.currCol += 1
            return True

    def moveDown(self):
        emptyBelow = True
        for i in range(self.currCol, self.currCol+4):
            if not isEmpty(self.chamber, self.currRow +1, i):
                emptyBelow = False
        if not emptyBelow:
            return False
        else: 
            self.currRow += 1
            return True





class PlusRock:
    def __init__(self, chamber):
        self.chamber = chamber
        self.currRow, self.currCol = START_POS
        self.height = 3
    
    def add(self, char):
        self.chamber[self.currRow][self.currCol+1] = char
        self.chamber[self.currRow+1][self.currCol] = char
        self.chamber[self.currRow+1][self.currCol+1] = char
        self.chamber[self.currRow+1][self.currCol+2] = char
        self.chamber[self.currRow+2][self.currCol+1] = char

        if char == '#':
            empties = getEmpties(self.chamber)
            if empties <= 3 + 3:
                for i in range(3 + 3 - empties):
                    self.chamber.insert(0, ['.','.','.','.','.','.', '.'])
            else:
                for i in range(abs(3 + 3 - empties)):
                    if self.chamber[0] == ['.','.','.','.','.','.', '.']:
                        self.chamber.pop(0)

    def moveLeft(self):
        # print(self.chamber[self.currRow+2][self.currCol])
        # print(isEmpty(self.chamber, self.currRow+2, self.currCol))
        if not (isEmpty(self.chamber, self.currRow+1, self.currCol-1)):
            return False

        if not (isEmpty(self.chamber, self.currRow+2, self.currCol)):
            return False

        # print("reached3")
        self.currCol -= 1
        return True

    def moveRight(self):
        if not isEmpty(self.chamber, self.currRow+1, self.currCol+3):
            return False
        else: 
            self.currCol += 1
            return True

    def moveDown(self):
        if not isEmpty(self.chamber, self.currRow+3, self.currCol + 1):
            return False

        if not isEmpty(self.chamber, self.currRow+2, self.currCol):
            return False
        
        if not isEmpty(self.chamber, self.currRow+2, self.currCol+2):
            return False
        self.currRow += 1
        return True


class LRock:
    def __init__(self, chamber):
        self.chamber = chamber
        self.currRow, self.currCol = START_POS
        self.height = 3
    
    def add(self, char):
        self.chamber[self.currRow+2][self.currCol+2] = char
        self.chamber[self.currRow+1][self.currCol+2] = char
        self.chamber[self.currRow][self.currCol+2] = char
        self.chamber[self.currRow+2][self.currCol+1] = char
        self.chamber[self.currRow+2][self.currCol] = char

        if char == '#':
            empties = getEmpties(self.chamber)
            if empties <= 4 + 3:
                for i in range(4 + 3 - empties):
                    self.chamber.insert(0, ['.','.','.','.','.','.', '.'])
            else:
                for i in range(abs(4 + 3 - empties)):
                    if self.chamber[0] == ['.','.','.','.','.','.', '.']:
                        self.chamber.pop(0)

    def moveLeft(self):
        if not isEmpty(self.chamber, self.currRow+2, self.currCol-1):
            return False
        else: 
            self.currCol -= 1
            return True

    def moveRight(self):
        for r in range(self.currRow, self.currRow+3):
            if not isEmpty(self.chamber, r, self.currCol+3):
                return False
        else: 
            self.currCol += 1
            return True

    def moveDown(self):
        for i in range(self.currCol, self.currCol+3):
            if not isEmpty(self.chamber, self.currRow +3, i):
                return False
        self.currRow += 1
        return True

class TallRock:
    def __init__(self, chamber):
        self.chamber = chamber
        self.currRow, self.currCol = START_POS
        self.height = 4
    
    
    def add(self, char):
        for i in range(self.currRow, self.currRow + 4):
            self.chamber[i][self.currCol] = char

        if char == '#':
            empties = getEmpties(self.chamber)
            if empties <= 2 + 3:
                for i in range(2 + 3 - empties):
                    self.chamber.insert(0, ['.','.','.','.','.','.', '.'])
            else:
                for i in range(abs(2 + 3 - empties)):
                    if self.chamber[0] == ['.','.','.','.','.','.', '.']:
                        self.chamber.pop(0)

    def moveLeft(self):
        for r in range(self.currRow, self.currRow+4):
            if not isEmpty(self.chamber, r, self.currCol-1):
                return False
        self.currCol -= 1
        return True

    def moveRight(self):
        for r in range(self.currRow, self.currRow+4):
            if not isEmpty(self.chamber, r, self.currCol+1):
                return False
        self.currCol += 1
        return True

    def moveDown(self):
        if not isEmpty(self.chamber, self.currRow +4, self.currCol):
            return False
        self.currRow += 1
        return True



class SquareRock:
    def __init__(self, chamber):
        self.chamber = chamber
        self.currRow, self.currCol = START_POS
        self.height = 2
    
    def add(self, char):
        self.chamber[self.currRow][self.currCol] = char
        self.chamber[self.currRow][self.currCol+1] = char
        self.chamber[self.currRow+1][self.currCol] = char
        self.chamber[self.currRow+1][self.currCol+1] = char

        if char == '#':
            empties = getEmpties(self.chamber)
            if empties <= 1 + 3:
                for i in range(1 + 3 - empties):
                    self.chamber.insert(0, ['.','.','.','.','.','.', '.'])
            else:
                for i in range(abs(1 + 3 - empties)):
                    if self.chamber[0] == ['.','.','.','.','.','.', '.']:
                        self.chamber.pop(0)

    def moveLeft(self):
        for r in range(self.currRow, self.currRow+2):
            if not isEmpty(self.chamber, r, self.currCol-1):
                return False
        self.currCol -= 1
        return True

    def moveRight(self):
        for r in range(self.currRow, self.currRow+2):
            if not isEmpty(self.chamber, r, self.currCol+2):
                return False
        self.currCol += 1
        return True

    def moveDown(self):
        for i in range(self.currCol, self.currCol+2):
            if not isEmpty(self.chamber, self.currRow +2, i):
                return False
        self.currRow += 1
        return True
        


ROCKS_CLASSES = [MinusRock, PlusRock, LRock, TallRock, SquareRock]

def process(file):
    lines = list([l.strip() for l in open(file).readlines()])[0]
    return lines


def printChamber(chamber):
    for i, row in enumerate(chamber):
        joinedRow = "".join(row)
        border = "+" if i == len(chamber) - 1 else "|"
        print(f"{border}{joinedRow}{border}")
    print()

def solvePart1(jets, numRocks):

    def printCurr(rk):
        rk.add("@")
        printChamber(rk.chamber)
        rk.add(".")

    chamber = [[AIR] * CHAMBER_WIDTH for _ in range(4)] + [[FLOOR] * CHAMBER_WIDTH]
    printChamber(chamber)

    highest = 0
    ind = 0
    for r in range(numRocks):
        rock = ROCKS_CLASSES[r%5](chamber)

        # chamber.insert(0, [[AIR] * CHAMBER_WIDTH for _ in range(rock.height)])
        #add rows to chamber based on height
        #printCurr(rock)
        #print(rock.height)
        
        isFalling = True
        while isFalling:
            jetDir = jets[ind % len(jets)] #should just loop the jets
            if jetDir == LEFT:
                rock.moveLeft()
            elif jetDir == RIGHT:
                rock.moveRight()
            isFalling = rock.moveDown()
            ind += 1
            # print(f"direction: {jetDir}, jetInd: {ind}, isFalling? {isFalling}")
            # print(ind % len(jets))
            # printCurr(rock)
        #no longer falling, has found its spot
        highest = max(highest, len(rock.chamber)-(rock.currRow)-1)
        rock.add('#')
        # print(f"highest: {highest}")
        chamber = rock.chamber
        printChamber(chamber)
    return highest
    


    #create an empty chamber with floor and 3 rows, 7 width
    #for rock in range(numRocks)
    #select the rock based on the current cycle
    #fill the rock in the top of the chamber
    #push left or right (can return a value of still falling)
    #add in built in no drop / no left or right into class methods
    #set falling to drop
    #reset new top value


def solvePart2(file):
    return True


def solve(file):
    jets = process(file)
    print(f"Part 1: {solvePart1(jets, 2022)}")
    #print(f"Part 2: {solvePart2(jets)}")

solve("input/17/input1.txt")

