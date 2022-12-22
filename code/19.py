
from numpy import rec


def process(file):
    lines = [l.strip() for l in open(file).readlines()]
    recipe = {}
    for count, line in enumerate(lines):
        count = count + 1
        recipe[count] = {}
        recipe[count]['oreRCost'] = int(line.split('ore robot costs ')[1].split(' ')[0])
        recipe[count]['clayRCost'] = int(line.split('clay robot costs ')[1].split(' ')[0])
        obsidianRobotOreCost = int(line.split('obsidian robot costs ')[1].split(' ')[0])
        obsidianRobotClayCost = int(line.split(' ore and ')[1].split(' ')[0])
        recipe[count]['obsidianRCost'] = (obsidianRobotOreCost,obsidianRobotClayCost)
        geodeRobotOreCost = int(line.split('Each geode robot costs ')[1].split(' ')[0])
        geodeRobotClayCost = int(line.split(' ore and ')[2].split(' ')[0])
        recipe[count]['geodeRCost'] = (geodeRobotOreCost,geodeRobotClayCost)
        
    print(recipe)
    return recipe


def makeEmptyMats():
    materials = [0,0,0,0]
    # materials = {}
    # materials['ore'] = 0
    # materials['clay'] = 0
    # materials['obsidian'] = 0
    # materials['geode'] = 0

    robots = [1,0,0,0]
    # robots = {}
    # robots['ore'] = 1
    # robots['clay'] = 0
    # robots['obsidian'] = 0
    # robots['geode'] = 0

    return materials, robots
    



def getOptions(inventory, costs):
    options = ['nothing']
    if inventory[0] >= costs['geodeRCost'][0] and inventory[2] >= costs['geodeRCost'][1]:
        options.append('geode')
    if inventory[0] >= costs['obsidianRCost'][0] and inventory[1] >= costs['obsidianRCost'][1]:
        options.append('obsidian')
    if inventory[0] >= costs['clayRCost']:
        options.append('clay')
    if inventory[0] >= costs['oreRCost']:
        options.append('ore')

    if 'geode' in options: #always the right decision to build a geode robot
        return ['geode']
    if 'obsidian' in options:
        return['obsidian']
    # if options == ['nothing','clay','ore']:
    #     return ['clay']
    # if options == ['nothing','ore']:
    #     return['ore']

    # if options == ['nothing','clay']:
    #     return['clay']
    # if options == ['nothing','ore']: #assume that its never profitable to build an ore 
    #     return ['nothing']
    return options
    
    
def getMaxGeodes(costs, inventory, robots, mins):
    # if mins == 23:
    #     print('hey')
    if mins == 24:
        return inventory[3]
    for count, robot in enumerate(robots):
        inventory[count] += robot #collect resources
    #how do I handle the different options here
    maxGeodes = 0
    options = getOptions(inventory, costs)
    for option in options:
        if option == 'nothing':
            testMax = getMaxGeodes(costs, inventory, robots, mins + 1)
            # inventory, robots = makeEmptyMats()
        elif option == 'geode':
            #build geode robot
            # inventory['ore'] -= costs['geodeRCost'][0]
            # inventory['obsidian'] -= costs['geodeRCost'][1]
            # robots['geode'] += 1
            testMax = getMaxGeodes(costs, [inventory[0] - costs['geodeRCost'][0], inventory[1], inventory[2] - costs['geodeRCost'][1], inventory[3]], [robots[0], robots[1], robots[2], robots[3]+1], mins + 1)
            # inventory, robots = makeEmptyMats()
            #reset the robots and inventory

        elif option == 'obsidian':
            # inventory['ore'] -= costs['obsidianRCost'][0]
            # inventory['clay'] -= costs['obsidianRCost'][1]
            # robots['obsidian'] += 1
            testMax = getMaxGeodes(costs, [inventory[0] - costs['obsidianRCost'][0], inventory[1] - costs['obsidianRCost'][1], inventory[2], inventory[3]], [robots[0], robots[1], robots[2]+1, robots[3]], mins + 1)
            # inventory, robots = makeEmptyMats()


        elif option == 'clay':
            # inventory['ore'] -= costs['clayRCost']
            # robots['clay'] += 1
            testMax = getMaxGeodes(costs, [inventory[0] - costs['clayRCost'], inventory[1], inventory[2], inventory[3]], [robots[0], robots[1]+1, robots[2], robots[3]], mins + 1)
            # inventory, robots = makeEmptyMats()


        elif option == 'ore':
            # inventory['ore'] -= costs['oreRCost']
            # robots['ore'] += 1
            testMax = getMaxGeodes(costs, [inventory[0] - costs['oreRCost'], inventory[1], inventory[2], inventory[3]], [robots[0]+1, robots[1], robots[2], robots[3]], mins + 1)
            # inventory, robots = makeEmptyMats()

        if testMax > maxGeodes:
            print(testMax)
            maxGeodes = testMax


    
    return maxGeodes



def makeList(recipe):
    geodeList = {}
    for blueprint in recipe:
        inventory, robots = makeEmptyMats()
        startingMinutes = 0
        costs = recipe[blueprint]
        maxGeodes = getMaxGeodes(costs, inventory, robots, startingMinutes)
        geodeList[blueprint] = maxGeodes
    return geodeList




def solvePart1(recipe):
    geodeList = makeList(recipe)
    print(geodeList)
    return True

def solvePart2(recipe):
    return True
    
def solve(file):
    recipe = process(file)
    print(f"Part 1: {solvePart1(recipe)}")
    print(f"Part 2: {solvePart2(recipe)}")

solve("input/19/input1.txt")