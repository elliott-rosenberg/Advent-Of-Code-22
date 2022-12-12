def process(file):
    lines = [l.strip() for l in open(file).readlines()]
    return lines

def solvePart1(file):
    return True

def solvePart2(file):
    return True


def solve(file):
    print(f"Part 1: {solvePart1(process(file))}")
    print(f"Part 2: {solvePart2(process(file))}")

solve("input/11/input1.txt")