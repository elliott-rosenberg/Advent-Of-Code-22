class CRT:
    def __init__(self):
        self.crt = [[0 for j in range(40)] for i in range(6)]
    
    def addPixel(self, reg, cycle):
        regBounds = [reg-1, reg, reg+1]
        #print(f"reg: {reg}, crt position: {(cycle-1)%40}")
        if ((cycle-1)%40) in regBounds:
            #print('#')
            self.crt[(cycle-1)//40][(cycle-1)%40] = '#' #should fill the 40 x 6 array in order
            #add a hashtag to the array

        else:
            #print(".")
            self.crt[(cycle-1)//40][(cycle-1)%40] = '.'

        #print((cycle-1)//40, (cycle-1)%40)

    def getCRT(self):
        return self.crt


class Clock:
    def __init__(self):
        self.count = 0
        self.state = 'before'
        self.x = 1
        self.strengthMap = {}


    def updateCount(self, val):
        self.count += val
    
    def setState(self, state):
        self.state = state

    def updateReg(self, val):
        self.x += val
    
    def getCycle(self):
        return self.count
    
    def getReg(self):
        return self.x

    def addSignalStrength(self):
        #print(f"reached, {self.count, self.x}")
        self.strengthMap[self.count] = (self.count * self.x)
        #print(self.strengthMap)

    def getStrengthSum(self):
        #print(self.strengthMap.values())

        return sum(self.strengthMap.values())




def process(file):
    lines = [l.strip().split(" ") for l in open(file).readlines()] #strips and splits file
    for line in lines: #turns number values into integers
        if line[0] == "addx":
            line[1] = int(line[1])
    return lines


def execute(file):
    cycle = Clock()
    cycleList = [20, 60, 100, 140, 180, 220]

    for line in file:
        
        if line[0] == 'noop':
            cycle.updateCount(1) #starts the next cycle, I think that's it
            if cycle.getCycle() in cycleList: #20th, 60th, 100th, 140th, 180th, and 220th
                cycle.addSignalStrength()
        elif line[0] == 'addx':
            cycle.setState('start')
            cycle.updateCount(1) #starts the next cycle
            if cycle.getCycle() in cycleList: #20th, 60th, 100th, 140th, 180th, and 220th
                cycle.addSignalStrength()
            cycle.updateCount(1) #starts the second cycle
            if cycle.getCycle() in cycleList: #20th, 60th, 100th, 140th, 180th, and 220th
                cycle.addSignalStrength()
            cycle.setState('finished')
            cycle.updateReg(line[1])
 
        else:
            raise Exception(f"bad first index, should be addx or noop")

    return cycle.getStrengthSum()




def execute2(file):
    clock = Clock()
    crt = CRT()
    for line in file:
        #print(line)
        if line[0] == 'noop':
            clock.updateCount(1)
            crt.addPixel(clock.getReg(), clock.getCycle())
        elif line[0] == 'addx':
            clock.updateCount(1)
            crt.addPixel(clock.getReg(), clock.getCycle())
            clock.updateCount(1)
            crt.addPixel(clock.getReg(), clock.getCycle())
            clock.updateReg(line[1])
        else:
            raise Exception(f"bad first index, should be addx or noop")
    return crt.getCRT()






def solvePart1(file):
    return execute(file)

def solvePart2(file):
    crt = execute2(file)

    with open("input/10/output1.txt", 'w') as f:
        for line in crt:
            f.write(f"{line }\n")
    return 'in output file'

def solve(file):
    instructions = process(file)
    print(f"Part 1: {solvePart1(instructions)}")
    print(f"Part 2: {solvePart2(instructions)}")


solve("input/10/input1.txt")