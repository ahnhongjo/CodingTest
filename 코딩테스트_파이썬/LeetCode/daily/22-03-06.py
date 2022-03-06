class Solution:
    def countOrders(self, n: int) -> int:
        answer = 1
        for i in range(1,2*n+1):
            if i%2==0:
                answer = (answer*(i//2))%1000000007
            else:
                answer = (answer*i)%1000000007
        return answer