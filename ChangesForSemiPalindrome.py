class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        cost = []
        for x in range(n):
            row = [float("inf")] * n
            cost.append(row)
            
        for length in range(2, n + 1):
            divs = []
            for d in range(1, length):
                if length % d == 0:
                    divs.append(d)
            for i in range(n - length + 1):
                j = i + length - 1
                minc = float("inf")
                for d in divs:
                    c = 0
                    for offset in range(d):
                        l = i + offset
                        r = j - d + 1 + offset
                        while l < r:
                            if s[l] != s[r]:
                                c += 1
                            l += d
                            r -= d
                    if c < minc:
                        minc = c
                cost[i][j] = minc

        dp = []
        for x in range(n):
            row = [float("inf")] * (k + 1)
            dp.append(row)
            
        for i in range(n):
            dp[i][1] = cost[0][i]
            
        for j in range(2, k + 1):
            for i in range(n):
                for p in range(i):
                    val = dp[p][j - 1] + cost[p + 1][i]
                    if val < dp[i][j]:
                        dp[i][j] = val
                        
        return dp[n - 1][k]
p=Solution()
print(p.minimumChanges( "abcac",2))