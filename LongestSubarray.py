class Solution(object):
    def longestMonotonicSubarray(self, nums):
       
        if not nums:
            return 0
            
        maxlen = 1
        currentinc = 1
        currentdec = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                currentinc += 1
                currentdec = 1
            elif nums[i] < nums[i - 1]:
                currentdec += 1
                currentinc = 1
            else:
                currentinc = 1
                currentdec = 1
                
            if currentinc > maxlen:
                maxlen = currentinc
            if currentdec > maxlen:
                maxlen = currentdec
                
        return maxlen
p=Solution()
print(p.longestmonotonic([1,4,3,3,2]))