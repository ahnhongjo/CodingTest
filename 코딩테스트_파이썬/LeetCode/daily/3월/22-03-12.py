class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_num = {}
        num_node = {}
        first = Node(head.val)
        n = 1
        num_node[n] = first
        node_num[head] = n
        before = first
        input_before = head.next

        while input_before:
            tmp = Node(input_before.val)
            before.next = tmp
            n += 1
            num_node[n] = tmp
            node_num[input_before] = n
            input_before = input_before.next
            before = tmp

        loop = first
        input_loop = head

        while loop:
            if not input_loop.random:
                loop.random = num_node[node_num[input_loop.random]]

            loop = loop.next
            input_loop= input_loop.next

        return first
