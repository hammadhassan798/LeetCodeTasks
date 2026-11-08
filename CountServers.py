class Solution(object):
    def countServers(self, grid):
        
        rows = len(grid)
        cols = len(grid[0])
        
        rowcounts = [0] * rows
        colcounts = [0] * cols
       
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowcounts[r] += 1
                    colcounts[c] += 1
                    
        communicatingcount = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if rowcounts[r] > 1 or colcounts[c] > 1:
                        communicatingcount += 1
                        
        return communicatingcount
p=Solution()
print(p.countServers([[1,0],[1,1]]))