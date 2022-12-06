
def process(file):
    
    return open(file).readlines()[0]
    

def findMarker(data):
    count = 4
    for x in range(len(data)-3):
        check = data[x:x+4]
        if len(set(check)) == 4:
            #print(count)
            return count
        else: count += 1
    return False

def findMessageMarker(data):
    count = 14
    for x in range(len(data)-13):
        check = data[x:x+14]
        if len(set(check)) == 14:
            print(count)
            return count
        else: count += 1
    return False



def solve1(file):
    data = process(file)
    return findMarker(data)

def solve2(file):
    data = process(file)
    return findMessageMarker(data)


solve1("input/06/input1.txt")
solve2("input/06/input1.txt")