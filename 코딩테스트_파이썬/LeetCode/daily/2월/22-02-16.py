# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head.next:
            ret = head.next
        else:
            ret = head

        before_head = None
        next_head = None

        while head.next:
            first_head = head
            second_head = head.next

            if before_head:
                before_head.next = second_head

            next_head = second_head.next

            second_head.next = first_head
            first_head.next = next_head

            before_head = first_head
            head = next_head

            if not head:
                return ret

        return ret
