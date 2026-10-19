class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        
      
        found=[]
        for i in range(len(nums)):
            if nums[i]==target:
                found.append(i)
        return found
        
      
p=Solution()
print(p.targetIndices([1,2,5,2,3],2))    
            