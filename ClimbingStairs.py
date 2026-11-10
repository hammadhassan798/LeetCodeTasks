class Solution(object):
    def climbStairs(self, n, costs):
        
        allcosts = [0] + costs
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            for stepsize in range(1, 4):
                j = i + stepsize
                if j <= n:
                    jumpcost = allcosts[j] + (j - i) * (j - i)
                    totalcost = dp[i] + jumpcost
                    if totalcost < dp[j]:
                        dp[j] = totalcost
                        
        return dp[n]
p=Solution()
print(p.climbStairs(4,[1,2,3,4]))