class Solution(object):
    def minimumOperations(self, nums, x, k):
      
        n = len(nums)
        numwindows = n - x + 1
        windowcosts = [0] * numwindows
        
        for i in range(numwindows):
            sub = []
            for j in range(x):
                sub.append(nums[i + j])
            sub.sort()
            medianval = sub[x // 2]
            
            currcost = 0
            for val in sub:
                diff = val - medianval
                if diff < 0:
                    diff = -diff
                currcost += diff
            windowcosts[i] = currcost
            
        infval = 10 ** 15
        dp = [[infval] * (k + 1) for _ in range(numwindows + 1)]
        
        for i in range(numwindows + 1):
            dp[i][0] = 0
            
        for c in range(1, k + 1):
            runningmin = infval
            for i in range(1, numwindows + 1):
         
                costifskipped = dp[i - 1][c]
                
                previdx = i - x
                if previdx >= 0:
                    costiftaken = dp[previdx][c - 1] + windowcosts[i - 1]
                else:
                    if c == 1:
                        costiftaken = windowcosts[i - 1]
                    else:
                        costiftaken = infval
                        
                if costiftaken < costifskipped:
                    dp[i][c] = costiftaken
                else:
                    dp[i][c] = costifskipped
                    
        return dp[numwindows][k]