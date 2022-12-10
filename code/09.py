
dirMap = {
    "U":[0,1],
    "D":[0,-1],
    "L":[-1,0],
    "R":[1,0]
}

tailMap = {
    "TL":{
        "U":[-1, 1, "T"],
        "D":[0,0,"L"],
        "L":[-1,1,"L"],
        "R":[0,0,"T"]
    },
    "T":{
        "U":[0,1,"T"],
        "D":[0,0,"S"],
        "L":[0,0,"TL"],
        "R":[0,0,"TR"]
    },
    "TR":{
        "U":[1,1,"T"],
        "D":[0,0,"R"],
        "L":[0,0,"T"],
        "R":[1,1,"R"]
    },
    "L":{
        "U":[0,0,"TL"],
        "D":[0,0,"BL"],
        "L":[-1,0,"L"],
        "R":[0,0,"S"]
    },
    "S":{
        "U":[0,0,"T"],
        "D":[0,0,"B"],
        "L":[0,0,"L"],
        "R":[0,0,"R"]
    },
    "R":{
        "U":[0,0,"TR"],
        "D":[0,0,"BR"],
        "L":[0,0,"S"],
        "R":[1,0,"R"]
    },
    "BL":{
        "U":[0,0,"L"],
        "D":[-1,-1,"B"],
        "L":[-1,-1,"L"],
        "R":[0,0,"B"]
    },
    "B":{
        "U":[0,0,"S"],
        "D":[0,-1,"B"],
        "L":[0,0,"BL"],
        "R":[0,0,"BR"]
    },
    "BR":{
        "U":[0,0,"R"],
        "D":[1,-1,"B"],
        "L":[0,0,"B"],
        "R":[1,-1,"R"]
    }
}


# class Head:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
    
#     def move(self, direction):
        
#         self.x += dirMap[direction][0]
#         self.y += dirMap[direction][1]
#         print(f"head {self.x, self.y}")
        


class Tail:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.relPos = "S"
        self.reached = {(0,0)}
        self.moves = [0,0]

    def move(self, direction):
        self.x += tailMap[self.relPos][direction][0]
        self.y += tailMap[self.relPos][direction][1]
        self.moves = [tailMap[self.relPos][direction][0],tailMap[self.relPos][direction][1]]
        self.relPos = tailMap[self.relPos][direction][2]
        print(self.x, self.y)
        
        self.reached.add((self.x,self.y))
        
    def getReached(self):
        
        return len(self.reached)

    def getMove(self):
        return self.moves
    
    def changePos(self, direct):
        if direct == [-1,-1]:
            self.relPos = "BL"
        if direct == [-1,-0]:
            self.relPos = "L"
        if direct == [-1,1]:
            self.relPos = "TL"
        if direct == [0,-1]:
            self.relPos = "B"
        if direct == [0,0]:
            self.relPos = "S"
        if direct == [0,1]:
            self.relPos = "T"
        if direct == [1,-1]:
            self.relPos = "BR"
        if direct == [1,0]:
            self.relPos = "R"
        if direct == [1,1]:
            self.relPos = "TR"







def doIt(instructions):
    # ropeHead = Head()
    ropeTail = Tail()
    for line in instructions:
        for x in range(line[1]):
            # ropeHead.move(line[0])
            ropeTail.move(line[0])
    return ropeTail.getReached()

        
        # head.move #pretty much just needs to change coordinates. Takes in direction
        # tail.move #adjust coordinates based on where head was and direction. Make a set of coordinates and add to set


def secondDo(file):
    ropeTail1 = Tail()
    ropeTail2 = Tail()
    for line in file:
        print(line)
        for x in range(line[1]):
            ropeTail1.move(line[0])
            ropeTail2.move(line[0])
            ropeTail2.changePos(ropeTail1.getMove()) #not working, didn't map the tail movement correctly





def process(file):
    lines = [l.strip() for l in open(file).readlines()]
    lines = [l.split(" ") for l in lines]
    for line in lines:
        line[1] = int(line[1])
    return lines



def solvePart1(file):
    return doIt(file)

def solvePart2(file):
    return secondDo(file)
    return True

def solve(file):
    instructions = process(file)
    print(f"Part 1: {solvePart1(instructions)}")
    print(f"Part 1: {solvePart2(instructions)}")


solve("input/09/input1.txt")
