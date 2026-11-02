class Solution(object):
    def minMoves2(self, nums):
        
        nums.sort()
        medianval = nums[len(nums) // 2]
        
        totalmoves = 0
        for num in nums:
            diff = num - medianval
            if diff < 0:
                diff = -diff
            totalmoves += diff
            
        return totalmoves
p=Solution()
print(p.minMoves2([1,10,2,9]))