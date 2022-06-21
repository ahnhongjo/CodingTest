from typing import List

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return []

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        answer =[]
        for product in products:
            trie.insert(product)

        for i in range(len(searchWord)):
            tmp = trie.starts_with(searchWord[:i+1])
            print(tmp)
            if len(tmp) ==0:
                answer.append([])
                continue
            tmp.sort()
            if len(tmp) >3:
                answer.append(tmp[:3])
            else:
                answer.append(tmp)

        return answer



a = Solution()

print(a.suggestedProducts(["havana"],"tatiana"))