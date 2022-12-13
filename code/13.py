# import json
# import ast
# from operator import indexOf

# def process(file):
#     lines = [l.strip() for l in open(file).readlines()]
#     count = 0
#     pairs = []
#     pair = []
#     for line in lines:
#         if count == 0:
#             pair.append(ast.literal_eval(line))
#             count += 1
#             continue
#         if count == 1:
#             pair.append(ast.literal_eval(line))
#             pairs.append(pair)
#             pair = []
#             count +=1
#             continue
#         if count == 2:
#             count = 0
#     for p in pairs:
#         print(p)

#     return pairs



# def checkOrder(pairs):
#     orderedIndices = []
#     for pair in pairs:
#         print(f"starting pair: {pair}")
#         correct = False
#         left = pair[0]
#         right = pair[1]


        
#         correct = comparePairs(left, right)
#         if correct:
#             print(f"adding to list: {pair}")
#             orderedIndices.append(pairs.index(pair)+1)
#         print(f"current ordered index: {orderedIndices}")

#     return orderedIndices



# def comparePairs(left, right):
#     skipIt = False
#     print(f"left: {left}, right: {right}")

#     if len(left) == 0 or len(right) == 0:
#         print(f"at least one empty")
#         if len(right) != 0:
#             print(f"correct")
#             return True #correct order
#         elif len(left) != 0:
#             print(f"incorrect")
#             return False
#         else: 
#             print(f"reached two empty lists")
#             skipIt = True
            
#     while not skipIt:
#         if (type(left[0]) == int) and (type(right[0]) == int): #both numbers
#             if left[0] < right[0]:
#                 print(f"correct")
#                 return True #correct order
#             elif left[0] > right[0]: #incorrect order
#                 print(f"incorrect")
#                 return False
#             else:
#                 print(f"same, going next")
#                 left.pop(0)
#                 right.pop(0)
#                 if len(left) == 0 or len(right) == 0:
#                     print(f"at least one empty")
#                     if len(right) != 0:
#                         print(f"correct")
#                         return True #correct order
#                     elif len(left) != 0:
#                         print(f"incorrect")
#                         return False
#                 else: return comparePairs(left, right)
#         else: #if (type(left[0]) == list) or (type(right[0]) == list) at least 1 list
#             if (type(left[0]) != list):
#                 left[0] = [left[0]]
#             elif (type(right[0]) != list): #changes them to both be lists
#                 right[0] = [right[0]]
            
#             if len(left) == 0 or len(right) == 0:
#                 print(f"at least one empty")
#                 if len(right) != 0:
#                     print(f"correct")
#                     return True #correct order
#                 elif len(left) != 0:
#                     print(f"incorrect")
#                     return False
#                 else: 
#                     left[0].pop(0)
#                     right[0].pop(0)
#                     return comparePairs(left, right)
#             else: 

#                 if left[0] != []:
#                     left.insert(0,left[0][0])
#                     left[1].pop(0)
#                 if right[0] != []:
#                     right.insert(0,right[0][0])
#                     right[1].pop(0)
#                 if left[0] != [] or right[0] != []:
#                     if left[1] == [] and right[1] == []:
#                         left.pop(1)
#                         right.pop(1)
#                 print(left[0], right[0])
#                 if left[0] == [] and right[0] == []:
#                     left.pop(0)
#                     right.pop(0)
#                     if len(left) == 0 or len(right) == 0:
#                         print(f"at least one empty")
#                         if len(right) != 0:
#                             print(f"correct")
#                             return True #correct order
#                         elif len(left) != 0:
#                             print(f"incorrect")
#                             return False
                    

#                 return comparePairs(left, right)


#     print(f"reached bottom")





# def solvePart1(pairs):
#     indices = checkOrder(pairs)
#     print(f"correct Indices: {indices}")
#     return True

# def solvePart2(file):
#     return True


# def solve(file):
#     print(f"Part 1: {solvePart1(process(file))}")
#     print(f"Part 2: {solvePart2(process(file))}")

# solve("input/13/input1.txt")


from functools import cmp_to_key, reduce
import operator

def parse(file):   
    def parseData(data):
        output = []
        listStack = [output]
        numAcc = ""
        for c in data:
            if c == "[":
                newList = []
                listStack[-1].append(newList)
                listStack.append(newList)
            elif c == "]":
                if len(numAcc):
                    listStack[-1].append(int(numAcc))
                numAcc = ""
                listStack.pop()
            elif c == ",":
                if len(numAcc):
                    listStack[-1].append(int(numAcc))
                numAcc = ""
            elif c != ",":
                numAcc += c
            
        return output.pop()

    lines = [l.strip() for l in open(file).readlines()]
    pairs = []
    for i in range(0, len(lines), 3):
        pairs.append((parseData(lines[i]), parseData(lines[i+1])))
    return pairs

def dataToString(data):
    if isinstance(data, list):
        return "[" + ",".join(map(dataToString, data)) + "]"
    else:
        return str(data)

def printDebug(s):
    # print(s)
    pass

LESS = 1
GREATER = -1
EQUAL = 0

def compare(left, right, leadspace):
    printDebug(f"{leadspace}- Compare {dataToString(left)} vs {dataToString(right)}")
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            printDebug(f"{leadspace}  - Left side is smaller, so inputs are in the right order")
            return LESS
        elif left > right:
            printDebug(f"{leadspace}  - Right side is smaller, so inputs are not in the right order")
            return GREATER
        else:
            return EQUAL
    elif isinstance(left, int) and isinstance(right, list):
        printDebug(f"{leadspace}  - Mixed types; convert left to {dataToString([left])} and retry comparison")
        return compare([left], right, leadspace + "  ")
    elif isinstance(left, list) and isinstance(right, int):
        printDebug(f"{leadspace}  - Mixed types; convert right to {dataToString([right])} and retry comparison")
        return compare(left, [right], leadspace + "  ")
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            res = compare(left[i], right[i], leadspace + "  ")
            if res == LESS or res == GREATER:
                return res
            i += 1
        if len(left) < len(right):
            printDebug(f"{leadspace}  - Left side ran out of items, so inputs are in the right order")
            return LESS
        elif len(left) > len(right):
            printDebug(f"{leadspace}  - Right side ran out of items, so inputs are not in the right order")
            return GREATER
        else:
            return EQUAL
    else:
        return None


def countPairsInOrder(pairs):
    indices = []
    for i, (left, right) in enumerate(pairs):
        printDebug(f"\n== Pair {i+1} ==")
        if compare(left, right, "") == LESS:
            indices.append(i + 1)
    return sum(indices)

def getPacketsInOrder(pairs):
    def comparePackets(packet1, packet2):
        return -compare(packet1, packet2, "")
    allPackets = []
    allPackets.append([[2]])
    allPackets.append([[6]])
    for pair in pairs:
        left, right = pair
        allPackets += [left, right]
    return sorted(allPackets, key=cmp_to_key(comparePackets))

def getDecoderKey(pairs):
    dividerPackets = ["[[2]]", "[[6]]"]
    dividerPacketIndices = []
    orderedPackets = getPacketsInOrder(pairs)
    for i, p in enumerate(orderedPackets):
        if dataToString(p) in dividerPackets:
            dividerPacketIndices.append(i + 1)
    return reduce(operator.mul, dividerPacketIndices)

def solve(file):
    pairs = parse(file)
    print(file)
    print(f"Part 1: {countPairsInOrder(pairs)}")
    print(f"Part 2: {getDecoderKey(pairs)}")

solve("input/13/input1.txt")