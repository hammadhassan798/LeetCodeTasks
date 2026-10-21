class Solution(object):
    def minOperations(self, s):
        n = len(s)
  
        is_sorted = True
        for i in range(n - 1):
            if s[i] > s[i + 1]:
                is_sorted = False
                break
        if is_sorted:
            return 0
  
        if n == 2:
            return -1
            
        mn = min(s)
        mx = max(s)
        

        if s[0] == mn or s[-1] == mx:
            return 1
            
  
        in_interior = False
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                in_interior = True
                break
                
        if in_interior:
            return 2
            
        return 3