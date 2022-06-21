from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        numlist=[]

        while list1 or list2:
            if list1 and list2:
                if list1.val >= list2.val:
                    numlist.append(list2.val)
                    list2 = list2.next
                else:
                    numlist.append(list1.val)
                    list1 = list1.next
            elif list1:
                numlist.append(list1.val)
                list1 = list1.next
            else:
                numlist.append(list2.val)
                list2 = list2.next

        start = ListNode(numlist[0])
        before = start
        for i in range(1,len(numlist)):
            tmp =ListNode(numlist[i])
            before.next=tmp
            before = tmp

        return start