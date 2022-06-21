from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s =""
        words.sort(key=len,reverse=True)

        for word in words:
            if word+"#" in s:
                continue

            else:
                s = s + word + "#"

        return len(s)

a = Solution()

a.minimumLengthEncoding(["time","me","bell"])