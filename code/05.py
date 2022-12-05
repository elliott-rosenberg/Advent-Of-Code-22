from curses.ascii import isdigit
from inspect import getouterframes
from operator import indexOf
from typing import final


def processCrates(file2):
    crateStacks = [l.strip() for l in open(file2).readlines()]
    crateStacks = [crate.split(',') for crate in crateStacks]
    return [0]+ crateStacks

def processInstructions(file1):
    instructions = [l for l in open(file1).readlines()]
    instruct = []
    for line in instructions:
        dig = []
        for c in line:
            if not(c.isdigit()):
                count = 0
            if c.isdigit():
                if count == 1:
                    dig[-1] = dig[-1] + c
                
                else: dig.append(c)
                count = 1
        instruct.append(dig)

    return instruct
    

def moveCrates1(stacks, instructs):
    finalStacks = stacks
    for struct in instructs:
        for x in range(int(struct[0])):
            finalStacks[int(struct[2])] += finalStacks[int(struct[1])].pop()
    return finalStacks

def moveCrates2(stacks, instructs):
    finalStacks = stacks
    for struct in instructs:
        finalStacks[int(struct[2])] += finalStacks[int(struct[1])][len(finalStacks[int(struct[1])])-int(struct[0]):] 
        for l in range(int(struct[0])):
            finalStacks[int(struct[1])].pop() 
    return finalStacks


def getOutput(final):
    solved = ''
    print(final)
    final.pop(0)
    for f in final:
        solved += f[-1]
    print(solved)
    return solved




def solve1(file1, file2):
    stacks = processCrates(file2)
    instructions = processInstructions(file1)
    finalCrates = moveCrates1(stacks, instructions)
    return getOutput(finalCrates)

def solve2(file1, file2):
    stacks = processCrates(file2)
    instructions = processInstructions(file1)
    finalCrates = moveCrates2(stacks, instructions)
    return getOutput(finalCrates)
    return 1



solve1("input/05/input1.txt", "input/05/input2.txt")
solve2("input/05/input1.txt", "input/05/input2.txt")
