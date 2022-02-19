from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        max_cnt = 0
        if not root:
            return 0
        q.append((root, 1))
        while q:
            pop_q = q.popleft()
            node = pop_q[0]
            cnt = pop_q[1]

            if cnt > max_cnt:
                max_cnt = cnt
            if node.left:
                q.append((node.left, cnt + 1))
            if node.right:
                q.append((node.right, cnt + 1))

        return max_cnt
