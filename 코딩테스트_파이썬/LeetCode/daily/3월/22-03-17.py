class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def splitparen(s):
            stack =[]
            ret =[]
            tmp =""
            for i in s:
                if len(stack) ==0 or i =="(":
                    stack.append(1)
                    tmp +="("
                else:
                    stack.pop()
                    tmp +=")"
                    if len(stack) ==0:
                        ret.append(tmp)
                        tmp =""
            return ret
        def scoreparen(s):
            split_s = splitparen(s)
            score =0
            if len(split_s) ==1:
                if s[1] ==")":
                    return 1
                else:
                    return 2*scoreparen(s[1:-1])
            else:
                for i in split_s:
                    score +=scoreparen(i)

            return score

        return scoreparen(s)




a = Solution()
print(a.scoreOfParentheses("()(())"))
