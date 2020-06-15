from typing import List
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniq = []
        self.counts = {}
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        ans = self.uniq[0] if len(self.uniq) > 0 else -1
        print(ans)
        return ans

    def add(self, value: int) -> None:
        if value in self.counts:
            self.counts[value] += 1
            self.uniq.remove(value)
        else:
            self.counts[value] = 1
            self.uniq.append(value)

# Your FirstUnique object will be instantiated and called as such:
firstUnique = FirstUnique([809])
firstUnique.showFirstUnique() # return 809
firstUnique.add(809)          # the queue is now [809,809]
firstUnique.showFirstUnique() # return -1