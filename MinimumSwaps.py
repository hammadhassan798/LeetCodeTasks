class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)
        
        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        
        indexed_nums = []
        for num in nums:
            indexed_nums.append((digit_sum(num), num))
        
        sorted_nums = sorted(indexed_nums)
        
        target_pos = {}
        for i, (_, val) in enumerate(sorted_nums):
            target_pos[val] = i
            
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i]:
                continue

            curr = i
            cycle_len = 0
            while not visited[curr]:
                visited[curr] = True
                val = nums[curr]
                curr = target_pos[val]
                cycle_len += 1
           
            if cycle_len > 1:
                swaps += (cycle_len - 1)
                
        return swaps