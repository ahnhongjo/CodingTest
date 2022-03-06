from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for word in words:
            is_pref = True
            if len(word) < len(pref):
                continue
            for i in range(len(pref)):
                if word[i] != pref[i]:
                    is_pref = False
            if is_pref:
                cnt +=1
        return cnt