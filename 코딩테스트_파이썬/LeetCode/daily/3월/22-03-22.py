class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ansstr=""

        for i in range(1,n+1):
            if (n-i) *26 >= k-1:
                ansstr +="a"
                k-=1
            else:
                tmp = k-26*(n-i)
                ansstr +=chr(tmp+96)
                k -= tmp
        return ansstr


a = Solution()

print(a.getSmallestString(5,73))
