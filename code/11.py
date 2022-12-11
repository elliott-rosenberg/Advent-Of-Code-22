class Monkey:
    def __init__(self, ident, items, operation, test, tf):
        self.id = ident
        self.items = items
        self.operation = operation
        self.test = test
        self.tf = tf

    def getInfo(self):
        return (f"id: {self.id}, items: {self.items}, operation: {self.operation}, test: {self.test}, next: {self.tf}")

    def getItemList(self):
        return self.items
    
    def inspectItem(self, item):
        



def process(file):
    lines = [l.strip() for l in open(file).readlines()] #strips and splits file
    count = 0
    tCount = 0
    monkeyList = []
    nextList = []
    for line in lines:
        # print(count)
        # print(line)
        if count == 0:
            identification = int(line[-2]) #get the monkey identification number of the monkey
            #print(identification)
            count += 1
            continue
        if count == 1:
            items = line.split(':')[1].split(',') #get the items that the monkey possesses, represented by the worry value
            for ct, item in enumerate(items):
                item = int(item[1:])
                items[ct] = item
            #print(items)
            count += 1
            continue
        if count == 2:
            instructs = line.split('= ')[1].replace('old', 'x')
            #print(instructs)
            count += 1
            continue
        if count == 3:
            test = int(line.split('by ')[1])
            #print(test)
            count += 1
            continue
        if count == 4:
            nextList.append(int(line[-1]))
            if tCount == 1:
                count += 1
            tCount += 1
            #print(nextList)
            continue
        if count == 5:
            monkey = Monkey(identification, items, instructs, test, nextList)
            monkeyList.append(monkey)
            tCount = 0
            count = 0
            nextList = []
    monkey = Monkey(identification, items, instructs, test, nextList)
    monkeyList.append(monkey)

    return monkeyList

def completeRound(monkeys):
    for monkey in monkeys:
        items = monkey.getItemList()
        for item in items:
            items.pop(0)
            inspected = monkey.inspectItem(item) #the score after monkey checks item and gets bored
            tested = monkey.testItem(inspected) #0 for passed, 1 for failed
            monkeys[monkey.newMonkey(tested)].addItem(inspected)# throws item to monkey given by tested val, and worry value of inspected





def solvePart1(info):
    monkeys = info
    rounds = 1
    x = 0
    while x < rounds:
        monkeys = completeRound(monkeys)
        x += 1
    return True

def solve(file):
    instructions = process(file)
    print(f"Part 1: {solvePart1(instructions)}")
    #print(f"Part 2: {solvePart2(instructions)}")


solve("input/11/input1.txt")