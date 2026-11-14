class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
      
        minsum = float("inf")
        n = len(nums)
        
        for i in range(n):
            for j in range(i, n):
                sublen = (j - i) + 1
                if l <= sublen <= r:
                    subarr = nums[i:j+1]
                    subsum = sum(subarr)
                    if subsum > 0:
                        if subsum < minsum:
                            minsum = subsum
                            
        if minsum == float("inf"):
            return -1
        return minsum

p = Solution()
print(p.minimumSumSubarray([3, -2, 1, 4], 2, 3))

    
               
        