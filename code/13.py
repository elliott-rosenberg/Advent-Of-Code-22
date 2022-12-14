import json
import ast
from operator import indexOf

def process(file):
    lines = [l.strip() for l in open(file).readlines()]
    count = 0
    pairs = []
    pair = []
    for line in lines:
        if count == 0:
            pair.append(ast.literal_eval(line))
            count += 1
            continue
        if count == 1:
            pair.append(ast.literal_eval(line))
            pairs.append(pair)
            pair = []
            count +=1
            continue
        if count == 2:
            count = 0
    for p in pairs:
        print(p)

    return pairs



def checkOrder(pairs):
    orderedIndices = []
    for pair in pairs:
        print(f"starting pair: {pair}")
        correct = False
        left = pair[0]
        right = pair[1]


        
        correct = comparePairs(left, right)
        if correct:
            print(f"adding to list: {pair}")
            orderedIndices.append(pairs.index(pair)+1)
        print(f"current ordered index: {orderedIndices}")

    return orderedIndices



def comparePairs(left, right):
    skipIt = False
    print(f"left: {left}, right: {right}")

    if len(left) == 0 or len(right) == 0:
        print(f"at least one empty")
        if len(right) != 0:
            print(f"correct")
            return True #correct order
        elif len(left) != 0:
            print(f"incorrect")
            return False
        else: 
            print(f"reached two empty lists")
            skipIt = True
            
    while not skipIt:
        if (type(left[0]) == int) and (type(right[0]) == int): #both numbers
            if left[0] < right[0]:
                print(f"correct")
                return True #correct order
            elif left[0] > right[0]: #incorrect order
                print(f"incorrect")
                return False
            else:
                print(f"same, going next")
                left.pop(0)
                right.pop(0)
                if len(left) == 0 or len(right) == 0:
                    print(f"at least one empty")
                    if len(right) != 0:
                        print(f"correct")
                        return True #correct order
                    elif len(left) != 0:
                        print(f"incorrect")
                        return False
                else: return comparePairs(left, right)
        else: #if (type(left[0]) == list) or (type(right[0]) == list) at least 1 list
            if (type(left[0]) != list):
                left[0] = [left[0]]
            elif (type(right[0]) != list): #changes them to both be lists
                right[0] = [right[0]]
            
            if len(left) == 0 or len(right) == 0:
                print(f"at least one empty")
                if len(right) != 0:
                    print(f"correct")
                    return True #correct order
                elif len(left) != 0:
                    print(f"incorrect")
                    return False
                else: 
                    left[0].pop(0)
                    right[0].pop(0)
                    return comparePairs(left, right)
            else: 

                if left[0] != []:
                    left.insert(0,left[0][0])
                    left[1].pop(0)
                if right[0] != []:
                    right.insert(0,right[0][0])
                    right[1].pop(0)
                if left[0] != [] or right[0] != []:
                    if left[1] == [] and right[1] == []:
                        left.pop(1)
                        right.pop(1)
                print(left[0], right[0])
                if left[0] == [] and right[0] == []:
                    left.pop(0)
                    right.pop(0)
                    if len(left) == 0 or len(right) == 0:
                        print(f"at least one empty")
                        if len(right) != 0:
                            print(f"correct")
                            return True #correct order
                        elif len(left) != 0:
                            print(f"incorrect")
                            return False
                    

                return comparePairs(left, right)


    print(f"reached bottom")





def solvePart1(pairs):
    indices = checkOrder(pairs)
    print(f"correct Indices: {indices}")
    return True

def solvePart2(file):
    return True


def solve(file):
    print(f"Part 1: {solvePart1(process(file))}")
    print(f"Part 2: {solvePart2(process(file))}")

solve("input/13/input1.txt")

