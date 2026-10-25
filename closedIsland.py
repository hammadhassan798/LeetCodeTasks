class Solution(object):
    def closedIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if grid[r][c] == 0:
                        self.floodFill(grid, r, c, rows, cols)
  
        islandcount = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    islandcount += 1
                    self.floodFill(grid, r, c, rows, cols)
                    
        return islandcount

    def floodFill(self, grid, startrow, startcol, rows, cols):
        queue = [[startrow, startcol]]
        grid[startrow][startcol] = 1
        rowshifts = [-1, 1, 0, 0]
        colshifts = [0, 0, -1, 1]
        
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            currrow = curr[0]
            currcol = curr[1]
            
            for i in range(4):
                nextrow = currrow + rowshifts[i]
                nextcol = currcol + colshifts[i]
                
                if nextrow >= 0 and nextrow < rows and nextcol >= 0 and nextcol < cols:
                    if grid[nextrow][nextcol] == 0:
                        grid[nextrow][nextcol] = 1
                        queue.append([nextrow, nextcol])
                        
p=Solution()
grid = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]
print(p.closedIsland(grid))