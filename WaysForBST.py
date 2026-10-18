class Solution(object):
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        
        comb = [[0] * n for _ in range(n)]
        for i in range(n):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
        
        def solve(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            interleave = comb[len(left) + len(right)][len(left)]
            
            ways = (interleave * solve(left) * solve(right)) % MOD
            
            return ways

       
        return (solve(nums) - 1) % MOD