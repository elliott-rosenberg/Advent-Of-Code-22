

class Node:
    def __init__(self, val, index):
        self.value = val
        self.index = index
        self.next = None
        #self.prev = None

    



class Linked:
    def __init__(self, head=None):
        self.head = head

    def append(self, newNode):
        current = self.head
        if current:
            while current.next :
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        count=1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count+1 == position:
                new_element.next =current.next
                current.next = new_element
                return
            else:
                count+=1
                current = current.next
            # break

        pass

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    

e1 = Node(1, 0)
e2 = Node(2, 1)
e3 = Node(6, 2)

e4 = Node(10, 3)

ll = Linked(e1)
ll.append(e2)
ll.append(e3)
ll.print()
ll.insert(e4, 2)
ll.delete(6)
print(' ')
ll.print()





def process(file):
    lines = [int(l.strip()) for l in open(file).readlines()]
    # for line in lines:
    #     print(line)
    return lines

def solvePart1(linked):
    return True


def solve(file):
    linked = process(file)
    print(f"Part 1: {solvePart1(linked)}")
    #print(f"Part 2: {solvePart2(recipe)}")

solve("input/20/input1.txt")