class Solution(object):
    def uniquePaths(self, grid):
       
        modval = 1000000007
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0, 0] for i in range(cols + 1)]
        dp[1][0] = 1
        dp[1][1] = 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dp[c + 1] = [dp[c + 1][1], dp[c][0]]
                else:
                    val = (dp[c + 1][1] + dp[c][0]) % modval
                    dp[c + 1] = [val, val]
                    
        return dp[cols][0]