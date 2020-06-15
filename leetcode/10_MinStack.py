from heapq import heapify, heappush, heappop 
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.minarr = []
        heapify(self.minarr)

    def push(self, x):
        self.arr.insert(0, x)
        heappush(self.minarr, x)

    def pop(self):
        e = self.arr.pop()
        self.minarr.remove(e)
        heapify(self.minarr)
        return e

    def top(self):
        return self.arr[-1]

    def getMin(self):
        return self.minarr[0]
        

# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.arr)
print(obj.getMin())
print(obj.arr)
print(obj.pop())
print(obj.arr)
print(obj.top())
print(obj.arr)
