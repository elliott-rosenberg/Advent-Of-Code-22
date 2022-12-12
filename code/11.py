class Monkey:
    def __init__(self, ident, items, operation, test, tf):
        self.id = ident
        self.items = items
        self.operation = operation
        self.test = test
        self.tf = tf
        self.inspected = 0
        self.modulo = 0

    def getInfo(self):
        return (f"id: {self.id}, items: {self.items}, operation: {self.operation}, test: {self.test}, next: {self.tf}, inspectedCount: {self.inspected}")

    def getItemList(self):
        return self.items

    def getInspected(self):
        return self.inspected

    def setProd(self, prod):
        self.modulo = prod

    
    def inspectItem(self, x):
        # print(f"x: {x}, y: {self.operation[2]}")
        if self.operation[2] == 'x':
            y = x
        else: y = int(self.operation[2])

        if self.operation[1] == '*':
            inspected = (x * y)

        else: inspected = (x + y)

        self.inspected += 1
        inspected = (inspected%self.modulo)
        return (inspected)

    def worryItem(self, item):
        return (item//3)


    def testItem(self, item):
        # print(self.test)
        # print(item)
        if (item % self.test == 0):
            return 0
        else: return 1

    def newMonkey(self, index):
        return self.tf[index]

    def addItem(self, item):
        self.items.append(item)


    def clearItems(self):
        self.items = []




def process(file):
    lines = [l.strip() for l in open(file).readlines()] #strips and splits file
    count = 0
    tCount = 0
    monkeyList = []
    nextList = []
    monkeyProd = 1
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
            instructs = instructs.split(' ')
            # print(instructs)
            count += 1
            continue
        if count == 3:
            test = int(line.split('by ')[1])
            if monkeyProd == 1:
                monkeyProd = test
            else: monkeyProd = monkeyProd * test
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

    for monkey in monkeyList:
        monkey.setProd(monkeyProd)

    return monkeyList

def completeRound(monkeys):
    
    for monkey in monkeys:
        items = monkey.getItemList()
        for item in items:
            # print(items)
            notWorried = monkey.inspectItem(item) #the score after monkey checks item and gets bored
            inspected = monkey.worryItem(notWorried)
            # print(inspected)
            
            tested = monkey.testItem(inspected) #0 for passed, 1 for failed
            # print(f"tested: {tested}")
            monkeys[monkey.newMonkey(tested)].addItem(inspected)# throws item to monkey given by tested val, and worry value of inspected
        monkey.clearItems()



    return monkeys

def getBusiness(monkeys):
    inspectedList = list(map(lambda m: m.getInspected(), monkeys))
    first = max(inspectedList)
    inspectedList.remove(first)
    second = max(inspectedList)
    return (first*second)



def solvePart1(info, numRounds):

    monkeys = info
    # for monkey in monkeys:
    #     print(monkey.getInfo())
    rounds = numRounds
    x = 0
    while x < rounds:
        monkeys = completeRound(monkeys)
        # for monkey in monkeys:
        #     print(monkey.getInfo())
        x += 1
    return getBusiness(monkeys)


def completeRound2(monkeys):

    for monkey in monkeys:
        items = monkey.getItemList()
        for item in items:
            # print(items)
            inspected = monkey.inspectItem(item) #the score after monkey checks item and gets bored
            # print(inspected)
            
            tested = monkey.testItem(inspected) #0 for passed, 1 for failed
            # print(f"tested: {tested}")
            monkeys[monkey.newMonkey(tested)].addItem(inspected)# throws item to monkey given by tested val, and worry value of inspected
        monkey.clearItems()

    

    return monkeys

def solvePart2(info, numRounds):
    monkeys = info
    rounds = numRounds
    x = 0
    while x < rounds:
        # print(x)
        monkeys = completeRound2(monkeys)
        # print(f"list of inspecteds{list(map(lambda m: m.getInspected(), monkeys))}")
        
        # for monkey in monkeys:
        #     print(monkey.getInfo())
        x += 1
    
    return getBusiness(monkeys)

def solve(file):
    print(f"Part 1: {solvePart1(process(file), 20)}")
    print(f"Part 2: {solvePart2(process(file), 10000)}")


solve("input/11/input1.txt")

