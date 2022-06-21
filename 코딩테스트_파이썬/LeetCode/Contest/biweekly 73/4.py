from collections import deque

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        def is_palen(s):
            for i in range(len(s) // 2):
                if s[i] != s[-1 - i]:
                    return False
            return True
        def swap(s,n):
            s = list(s)
            s[n], s[n + 1] = s[n + 1], s[n]
            return "".join(s)

        visit =set()

        q= deque()
        q.append((s,0))
        visit.add(s)

        while q:
            now = q.popleft()
            if is_palen(now[0]):
                return now[1]
            for i in range(len(now[0])-1):
                tmp = swap(now[0],i)
                if tmp not in visit:
                    q.append((tmp,now[1]+1))
                    visit.add(tmp)