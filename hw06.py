import heapq


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
1. Top k Frequent Elements
"""
def kFrequent(nums, k):
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key = lambda x:(freq[x], -x))



"""
2. All paths from one vertex to another in DAG
"""
def allPaths(edges, source, destination):
    final = []
    q = Queue()
    q.enqueue([source])
    while not q.isEmpty():
        path = q.dequeue()
        if path[-1] == destination:
            final.append(path)
        else:
            for i in edges:
                if i[0] == path[-1]:
                    q.enqueue(path + [i[1]])
    return final


edges = [("a","b"), ("a","c"), ("b","d"), ("c","d")]
source = "a"
destination = "d"
allPaths(edges, source, destination)


