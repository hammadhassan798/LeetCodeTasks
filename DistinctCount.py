class Solution(object):
    def sumCounts(self, nums):
        totalsum = 0
        n = len(nums)
      
        for i in range(n):
            seen = set() 
            
            for j in range(i, n):
                seen.add(nums[j]) 
              
                distinctcount = len(seen)
                totalsum += distinctcount ** 2
                
        return totalsum