class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        valid=0
        for i in arr1:
            isclose = False
            for j in arr2:
                if abs(i-j) <= d:
                    isclose = True
                    break
            if not isclose:
                valid += 1    
            
        return valid
p=Solution()
print(p.findTheDistanceValue([1,4,2,3],[-4,-3,6,10,20,30],3))
                    