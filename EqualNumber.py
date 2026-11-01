class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = nums[0]
        for num in nums:
            if num < smallest:
                smallest = num
                
        totalmoves = 0
        for num in nums:
            totalmoves += num - smallest
            
        return totalmoves