class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_stack=[]
        shut_stack=[]

        for i in range(len(s)):
            if s[i]=="(":
                open_stack.append(i)
            elif s[i] ==")":
                if len(open_stack)==0:
                    shut_stack.append(i)
                else:
                    open_stack.pop()

        answer=""
        for i in range(len(s)):
            if i in shut_stack or i in open_stack:
                continue
            else:
                answer+=s[i]

        print(answer)
        return answer

a= Solution()

a.minRemoveToMakeValid("lee(t(c)o)de)")