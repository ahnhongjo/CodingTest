from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sort_list=[]

        while True:
            sort_list.append(head.val)

            if head.next:
                head = head.next
            else:
                break

        sort_list.sort(reverse=True)
        tmp = None

        for i in sort_list:
            if tmp:
                now = ListNode(i,tmp)
                tmp = now
            else:
                tmp = ListNode(i,None)
        return now


