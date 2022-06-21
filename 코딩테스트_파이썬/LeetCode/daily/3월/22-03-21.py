from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans =[]

        alpha = set()
        for i in range(len(s)):
            alpha.add(s[i])
            cut = True
            for j in alpha:
                if j in s[i+1:]:
                    cut = False
                    break


            if cut:
                ans.append(i)
                alpha = set()

            else:
                continue

        real_ans =[]

        for i in range(len(ans)):
            if i ==0:
                real_ans.append(ans[i]+1)
            else:
                real_ans.append(ans[i]-ans[i-1])

        return real_ans



a= Solution()

a.partitionLabels("ababcbacadefegdehijhklij")