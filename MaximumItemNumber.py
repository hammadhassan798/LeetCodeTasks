class Solution(object):
    def maximumSaleItems(self, items, budget):
       
        n = len(items)
        minprice = items[0][1]
        for i in range(1, n):
            if items[i][1] < minprice:
                minprice = items[i][1]

        gains = [1] * n
        for i in range(n):
            fi = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    gains[i] += 1

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            cost = items[i][1]
            val = gains[i]
            if cost <= budget:
                for b in range(budget, cost - 1, -1):
                    if dp[b - cost] != -1:
                        cand = dp[b - cost] + val
                        if cand > dp[b]:
                            dp[b] = cand

        ans = 0
        for spent in range(budget + 1):
            if dp[spent] != -1:
                rem = budget - spent
                total = dp[spent] + (rem // minprice)
                if total > ans:
                    ans = total

        return ans
p=Solution()
print(p.maximumSaleItems([[6,2],[2,6],[3,4]],9))