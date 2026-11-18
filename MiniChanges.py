class Solution(object):
    def minchanges(self, s):
       
        cost = 0
        
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                cost += 1
                
        return cost

p = Solution()
print(p.minchanges("1001")) 