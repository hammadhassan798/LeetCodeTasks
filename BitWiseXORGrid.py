class Solution(object):
    def minCost(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [set() for i in range(cols)]
        
        dp[0].add(grid[0][0])
        
        for c in range(1, cols):
            val = grid[0][c]
            for prevxor in dp[c - 1]:
                dp[c].add(prevxor ^ val)
           
        for r in range(1, rows):
            newdp0 = set()
            val = grid[r][0]
            for prevxor in dp[0]:
                newdp0.add(prevxor ^ val)
            dp[0] = newdp0
            
            for c in range(1, cols):
                val = grid[r][c]
                currentset = set()
                
                for prevxor in dp[c]:
                    currentset.add(prevxor ^ val)
              
                for prevxor in dp[c - 1]:
                    currentset.add(prevxor ^ val)
                    
                dp[c] = currentset

        return min(dp[cols - 1])
grid=[[1,2],[3,4]]
p=Solution()
print(p.minCost(grid))