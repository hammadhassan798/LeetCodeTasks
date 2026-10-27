class Solution(object):
    def createGrid(self, m, n):
        grid = [["#"] * n for _ in range(m)]
        
     
        for c in range(n):
            grid[0][c] = "."
        
        for r in range(m):
            grid[r][n - 1] = "."
     
        result = []
        for row in grid:
            result.append("".join(row))
            
        return result
    
p=Solution()
print(p.createGrid(3,3))