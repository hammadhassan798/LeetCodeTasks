class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        zero = nums.index(0)
       
        def check(step):
            for i in range(1, n):
                prev_idx = (zero + (i - 1) * step) % n
                curr_idx = (zero + i * step) % n
                if nums[prev_idx] > nums[curr_idx]:
                    return False
            return True
            
        ans = float('inf')
       
        if check(1):
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)
   
        if check(-1):
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)
            
        if ans == float('inf'):
            return -1
            
        return ans