class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = {}
        ret = 0
        for i in range(26):
            alpha[chr(i + 65)] = i + 1

        for i in columnTitle:
            ret = ret * 26 + alpha[i]
        return ret