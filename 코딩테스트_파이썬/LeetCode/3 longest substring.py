class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha_dict={}
        maxlen = 0
        nowlen = 0
        pos = 0

        for i in s:
            if i in alpha_dict:
                alpha_dict[i]+=1
            else:
                alpha_dict[i]=1
            nowlen +=1
            while alpha_dict[i]>1:
                alpha_dict[s[pos]] -=1
                nowlen-=1
                pos+=1
            maxlen = max(maxlen,nowlen)

        return maxlen


a = Solution()

a.lengthOfLongestSubstring("abcde")

print(ord(" "))