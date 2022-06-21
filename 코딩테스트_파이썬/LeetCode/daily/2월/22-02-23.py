
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodes = {}
        visited = set()

        q = [node]

        while q:
            now_node = q.pop()
            i = now_node.val
            if i in visited:
                continue
            visited.add(i)
            nodes[i] = Node()
            nodes[i].val=i
            for nd in now_node.neighbors:
                if nd.val not in visited:
                    q.append(nd)

        visited = set()
        q = [node]
        while q:
            now_node = q.pop()
            i = now_node.val
            if i in visited:
                continue
            nodes[i].neighbors=[]

            for nd in now_node.neighbors:
                nodes[i].neighbors.append(nodes[nd.val])
                q.append(nd)

            visited.add(i)

        ret_node = nodes[node.val]

        return ret_node


A = Node()
B = Node()
C = Node()
D = Node()

A.val = 1
B.val = 2
C.val = 3
D.val = 4

A.neighbors = [B, D]
B.neighbors = [A, C]
C.neighbors = [B, D]
D.neighbors = [A, C]

test = Solution()
test.cloneGraph([])
