"""
Queue class used for Problem 1
"""
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

"""
Node class used for Problem 2-5
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.next = node



"""
1. Stack2 class
Implement stack data structure using queue
"""
class Stack2:
    def __init__(self):
        self.q = Queue()
        return

    def isEmpty(self):
        return self.q.isEmpty()

    def size(self):
        return self.q.size()
    
    def push(self, item):
        self.q.enqueue(item)
        return

    def pop(self):
        for i in range(self.size() - 1):
            top = self.q.dequeue()
            self.q.enqueue(top)
        return self.q.dequeue() 

    def peek(self):
        for i in range(self.size()):
            top = self.q.dequeue()
            self.q.enqueue(top)
            last = self.q.dequeue()
            self.q.enqueue(last)
        return last



"""
2. transform(lst)
Transform an unordered list into a Python list
Input: an (possibly empty) unordered list
Output: a Python list
"""

node1 = Node(2)
node2 = Node(1)
node3 = Node(3)

node1.setNext(node2)
node2.setNext(node3)

nodeA = Node(6)
nodeB = Node(7)
nodeC = Node(4)
nodeD = Node(5)
nodeE = Node(10)

nodeA.setNext(nodeB)
nodeB.setNext(nodeC)
nodeC.setNext(nodeD)
nodeD.setNext(nodeE)

nod = Node(None)
nodd = Node(None)
noddd = Node(7)


def transform(head):
    lst = []
    h = head
    while h is not None:
        val = h.getData()
        lst.append(val)
        h = h.getNext()
    return lst

"""
3. concatenate(lst1, lst2)
Concatenate two unordered lists
Input: two (possibly empty) unordered list
Output: an unordered list
"""
def concatenate(head1, head2):
    one = head1
    two = head2
    if one is None and two is None:
        return 
    elif one is not None and two is None:
        return head1
    elif one is None and two is not None:
        return head2
    else:
        while one.getNext() is not None:
            one = one.getNext()
        one.setNext(two)
        return head1

    
def printLinkedList(head):  
    current = head
    while current != None:      
        print(current.getData())
        current = current.getNext()


"""
4. removeNodesFromBeginning(lst, n)
Remove the first n nodes from an unordered list
Input:
    lst -- an (possibly empty) unordered list
    n -- a non-negative integer
Output: an unordered list
"""
def removeNodesFromBeginning(h, n):
    curr = h
    if n == 1:
        curr = curr.getNext()
        h.setNext(None)
        return curr
    for i in range(n):
        curr = curr.getNext()
    return curr


"""
5. removeNodes(lst, i, n)
Starting from the ith node, remove the next n nodes
(not including the ith node itself).
Assume i + n <= lst.length(), i >= 0, n >= 0.
Input:
    lst -- an unordered list
    i -- a non-negative integer
    n -- a non-negative integer
Output: an unordred list

lst = [1, 2, 3, 4, 5]
i = 2
n = 2
return [1, 2, 5]

i = 1
n = 2
return [1, 4, 5]

i = 0
n = 2
return [3, 4, 5]
"""
def removeNodes(head, i, n):
    curr = head
    if i == 0:
        if n == 0:
            return curr
        return removeNodesFromBeginning(head,n)
    if n == 0:
        return curr
    for space in range(1,i):
        curr = curr.getNext()
    prev = curr.getNext()
    for space in range(1, n+1):
        follow = prev.getNext()
        prev = prev.getNext()
    curr.setNext(follow)
    return head
    
    








