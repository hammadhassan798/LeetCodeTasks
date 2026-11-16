class Solution(object):
    def digitsum(self, s, k):
        currents = s
     
        while len(currents) > k:
            ans = ""
    
            for i in range(0, len(currents), k):
                group = currents[i:i+k]
        
                total = 0
                for c in group:
                    total += int(c)
                    
                ans += str(total)
                
            currents = ans
            
        return currents

p = Solution()
print(p.digitsum("11111222223", 3))