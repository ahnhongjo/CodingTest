from typing import List

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = [set() for _ in range(26)]
        self.suffix = [set() for _ in range(26)]
        idx =0
        for word in words:
            self.prefix[ord(word[0])-ord("a")].add((word,idx))
            self.suffix[ord(word[-1]) - ord("a")].add((word, idx))

    def f(self, prefix: str, suffix: str) -> int:
        commons = self.prefix[ord(prefix)-ord("a")] & self.suffix[ord(suffix)-ord("a")]
        maxval = -1
        if len(commons) ==0:
            return -1

        for common in commons:
            if maxval < common[1]:
                maxval = common[1]

        return maxval




# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

a = WordFilter(["apple"])

a.f("a","e")
