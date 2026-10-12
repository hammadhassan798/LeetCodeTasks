class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        
        bit_counts = [0] * 31
        for num in nums:
            for bit in range(31):
                if (num >> bit) & 1:
                    bit_counts[bit] += 1
 
        k_numbers = [0] * k
        for bit in range(30, -1, -1):
            count = bit_counts[bit]
          
            for i in range(min(count, k)):
                k_numbers[i] |= (1 << bit)

        total_sum = 0
        for num in k_numbers:
            total_sum = (total_sum + (num * num) % MOD) % MOD
            
        return total_sum