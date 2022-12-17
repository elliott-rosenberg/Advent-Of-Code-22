def process(file):
    lines = [l.strip() for l in open(file).readlines()]

    readings = []

    for line in lines:
        xS = int(line.split('x=')[1].split(',')[0])
        yS = int(line.split('y=')[1].split(':')[0])
        xB = int(line.split('x=')[2].split(',')[0])
        yB = int(line.split('y=')[2])

        dist = getDistance([xS, yS], [xB, yB])
        readings.append([[xS, yS], [xB, yB], dist])

    return readings

def getDistance(sensor, beacon):
    return (abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1]))


def getImpossibleCount(data, check):
    rtc = check
    imPos = set()
    beacs = set()
    prt2 = set()

    for sensor, beacon, dist in data:
        #check if distance is within check row
        xSens = sensor[0]
        ySens = sensor[1]
        vertDist = abs(ySens - rtc)
        hoDist = dist -vertDist
        # print(f"hoDist {hoDist}")
        if hoDist > 0:
            for spot in range(xSens-hoDist, xSens + hoDist + 1):
                imPos.add(spot)
                prt2.add(spot)
        if beacon[1] == rtc:
            prt2.add(beacon[0])
            beacs.add(beacon[0])
    # print(list(newImpos))
    overlap = imPos.intersection(beacs)
    for o in overlap:
        imPos.remove(o)

    return (len(imPos), list(prt2))


def solvePart1(data, check):
    return getImpossibleCount(data, check)[0]

def solvePart2(reads):
    bounds = 4000000
    for row in range(bounds + 1):
        if row % 10000 == 0:
            print(f"Row {row}/{bounds}")
        reachableSensors = set()
        spots = set()
        for sensor, beacon, dist in reads:
            xSens = sensor[0]
            ySens = sensor[1]
            vertDist = abs(ySens - row)
            hoDist = dist -vertDist
            if hoDist >=0:
                reachableSensors.add((sensor, dist)) #builds list of in reach sensors and their distance from the row in question
                spots.add((xSens+hoDist + 1, row)) #spot just outside of range
                spots.add((xSens - hoDist - 1, row))
            
        for sp in spots:
            foundIt = True
            if sp[0] > 0 and sp[0] <= bounds:
                for sensor, beacon, dist in reachableSensors:
                    if getDistance(sensor, sp) <= dist:
                        foundIt = False
                        break
                if foundIt:
                    return (sp[0] * 4000000) + sp[1]
                





    #would work I think but too long
    # bounds = 4000000
    # firstRow = set((getImpossibleCount(reads, 1)[1])[:bounds + 1])
    # for row in range(bounds + 1):
    #     print(row)
    #     rtc = (getImpossibleCount(reads, row)[1])[:bounds + 1]
    #     # print(rtc)
    #     if rtc[-1] != bounds:
    #         x = list(set(rtc[:-1]) ^ firstRow)[0]
    #         freq = (x * 4000000) + row
    #         return freq
            

    # return True


def solve(file):
    reads = process(file)
    print(f"Part 1: {solvePart1(reads, 2000000)}")
    print(f"Part 2: {solvePart2(reads)}")

solve("input/15/input1.txt")


