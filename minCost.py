class Solution(object):
    def minimumCost(self, cost1, cost2, costboth, need1, need2):
      
        optionone = need1 * cost1 + need2 * cost2
        optiontwo = costboth * max(need1, need2)
        
        mn = min(need1, need2)
        optionthree = costboth * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2
        
        return min(optionone, optiontwo, optionthree)
p=Solution()
print(p.minimumCost(3,2,1,3,2))