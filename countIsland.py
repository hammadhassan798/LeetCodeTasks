class Solution(object):
    def countDivisibleIslands(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])
        divisiblecount = 0
        
        rowshifts = [-1, 1, 0, 0]
        colshifts = [0, 0, -1, 1]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    islandsum = 0
                    queue = [[r, c]]
                    islandsum += grid[r][c]
                    grid[r][c] = 0 
                    
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
                                if grid[nextrow][nextcol] > 0:
                                    islandsum += grid[nextrow][nextcol]
                                    grid[nextrow][nextcol] = 0
                                    queue.append([nextrow, nextcol])
                                    
                    if islandsum % k == 0:
                        divisiblecount += 1
                        
        return divisiblecount