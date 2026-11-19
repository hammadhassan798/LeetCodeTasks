class Solution(object):
    def minimizeSum(self, nums):
     
        nums.sort()
        n = len(nums)
        
        opt1 = nums[n - 1] - nums[2]
        opt2 = nums[n - 3] - nums[0]
        opt3 = nums[n - 2] - nums[1]
        
        ans = opt1
        if opt2 < ans:
            ans = opt2
        if opt3 < ans:
            ans = opt3
            
        return ans