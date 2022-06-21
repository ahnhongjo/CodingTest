from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width_len = {1: [0, 0]}
        q = deque()
        q.append((root, 1, 0))
        level = 1

        while q:
            now = q.popleft()

            if level != now[1]:
                width_len[level][1] = rightmost
                level = now[1]
                width_len[level] = [now[2],2**(level-1)]
            if now[0].left:
                q.append((now[0].left, now[1] + 1,now[2]*2))

            if now[0].right:
                q.append((now[0].right, now[1] + 1,now[2]*2+1))
            rightmost = now[2]

        width_len[level][1] = rightmost

        max_len = 0
        for wid_len in width_len.values():
            if wid_len[1]-wid_len[0]+1 > max_len:
                max_len = wid_len[1]-wid_len[0]+1

        return max_len

a = Solution()

tmp5 = TreeNode(5)
tmp3 = TreeNode(3)
tmp3_3 = TreeNode(3, tmp5, tmp3)
tmp1 = TreeNode(1, tmp3_3)

a.widthOfBinaryTree(tmp1)
