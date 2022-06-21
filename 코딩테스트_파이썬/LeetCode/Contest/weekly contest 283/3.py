from typing import List
from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_dict={}
        parent_dict=defaultdict(int)

        for node in descriptions:
            parent = node[0]
            parent_dict[node[1]] =node[0]
            if node[0] not in node_dict:
                node_dict[node[0]] = TreeNode(node[0])
            if node[1] not in node_dict:
                node_dict[node[1]] = TreeNode(node[1])
            if node[2] ==1:
                node_dict[node[0]].left = node_dict[node[1]]
            else:
                node_dict[node[0]].right = node_dict[node[1]]

        while True:
            if parent_dict[parent] ==0:
                return node_dict[parent]
            parent = parent_dict[parent]
