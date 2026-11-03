class Solution(object):
    def minMoves(self, nums):
        totalsum=0
        
        maxval=max(nums)
        for i in nums:
            totalsum+=maxval-i
        return totalsum
p=Solution()
print(p.minMoves([4,4,5]))