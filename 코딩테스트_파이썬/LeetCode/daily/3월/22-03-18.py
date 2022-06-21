class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        alpha=set()
        for i in s:
            if i not in alpha:
                alpha.add(i)

        alpha_list = list(alpha)
        alpha_list.sort()

        list_index=[]
        for i in alpha_list:
            list_index.append(s.index(i))

        print(list_index)



a = Solution()

a.removeDuplicateLetters("cbacdcbc")