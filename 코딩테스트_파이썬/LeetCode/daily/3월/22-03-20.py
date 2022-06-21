from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        same_num = []
        for i in range(len(tops)):
            if i == 0:
                same_num.append(tops[i])
                same_num.append(bottoms[i])
            else:
                if tops[i] in same_num and bottoms[i] in same_num:
                    if tops[i] == bottoms[i]:
                        same_num=[tops[i]]
                    else:
                        continue
                elif tops[i] in same_num:
                    same_num = [tops[i]]
                elif bottoms[i] in same_num:
                    same_num = [bottoms[i]]
                else:
                    return -1

        if len(same_num) == 2:
            ans = 0
            for i in range(len(tops)):
                if tops[i] == same_num[0]:
                    ans += 1
            return min(ans, len(tops) - ans)
        else:
            top_num = 0
            bot_num = 0
            for i in range(len(tops)):
                if tops[i] == same_num[0]:
                    top_num += 1
                if bottoms[i] == same_num[0]:
                    bot_num += 1
            return len(tops) - max(top_num, bot_num)


a = Solution()
print(a.minDominoRotations(
    [1, 2, 1, 1, 1, 2, 2, 2],
    [2, 1, 2, 2, 2, 2, 2, 2]))
