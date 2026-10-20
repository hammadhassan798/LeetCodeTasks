class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        targ = sorted(nums)
        totalSumk= 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            isSortable = True
          
            for j in range(0, n, k):
                originalBlock = nums[j : j + k]
                targetBlock = targ[j : j + k]
                
                doubledBlock =   originalBlock  +   originalBlock 
                
                found = False
                for i in range(k):
                    if doubledBlock[i :i + k] ==  targetBlock:
                        found = True
                        break
                
                if not found:
                    isSortable = False
                    break
            
            if isSortable:
                for j in range(0, n - k, k):
                    currMax = max(nums[j : j + k])
                    nextMin = min(nums[j + k : j + 2 * k])
                    if currMax > nextMin:
                        isSortable = False
                        break
            
            if isSortable:
                totalSumk += k
                
        return  totalSumk
p=Solution()
print(p.sortableIntegers([7,6,5]))