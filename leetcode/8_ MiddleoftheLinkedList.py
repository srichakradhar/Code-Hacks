# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        first = head
        second = head
        while second.next is not None:
            print(first.val, second.val)
            first = first.next
            second = second.next
            if second.next is None:
                return first
            second = second.next
        return first

a = [1,2,3,4,5, 6]
head = ListNode(a[0])
node = head
for i in range(1, len(a)):
    node.next = ListNode(a[i])
    node = node.next

s = Solution()
mid = s.middleNode(head)
print(mid.val)
# while res.next is not None:
