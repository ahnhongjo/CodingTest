from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        before = start
        before.val = (l1.val + l2.val)%10
        c = (l1.val+l2.val)//10
        l1 = l1.next
        l2 = l2.next
        while l1 or l2 or c!=0:
            tmp = ListNode()
            before.next = tmp
            if l1 and l2:
                tmp.val = (l1.val+l2.val+c)%10
                c = (l1.val+l2.val+c)//10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                tmp.val = (l1.val + c) % 10
                c = (l1.val +  c) // 10
                l1 = l1.next
            elif l2:
                tmp.val = (l2.val + c) % 10
                c = (l2.val + c) // 10
                l2 = l2.next
            else:
                tmp.val = c
                c = 0
            before = tmp
        return start


a1 = ListNode(3)
a2 = ListNode(4, a1)
a3 = ListNode(2, a2)

b1 = ListNode(4)
b2 = ListNode(6, b1)
b3 = ListNode(5, b2)

tmp = Solution()
tmp.addTwoNumbers(a3, b3)
