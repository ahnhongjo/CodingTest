class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}
        t_dict = {}
        cnt = 0

        for i in range(26):
            s_dict[chr(i + 97)] = 0
            t_dict[chr(i + 97)] = 0

        for s_chr in s:
            s_dict[s_chr] +=1
        for t_chr in t:
            t_dict[t_chr] +=1

        for i in range(26):
            cnt += abs(s_dict[chr(i+97)]-t_dict[chr(i+97)])

        return cnt


a = Solution()
a.minSteps("AAA", "BBB")
