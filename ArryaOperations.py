class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        
        # Step 1: Count the frequency of set bits across all numbers (bits 0 to 30)
        bit_counts = [0] * 31
        for num in nums:
            for bit in range(31):
                if (num >> bit) & 1:
                    bit_counts[bit] += 1
                    
        # Step 2: Greedily construct the k largest possible numbers
        # We will store the values of these k numbers
        k_numbers = [0] * k
        for bit in range(30, -1, -1):
            count = bit_counts[bit]
            # Assign this bit to the top 'count' slots (up to k slots)
            for i in range(min(count, k)):
                k_numbers[i] |= (1 << bit)
                
        # Step 3: Calculate the sum of squares modulo 10^9 + 7
        total_sum = 0
        for num in k_numbers:
            total_sum = (total_sum + (num * num) % MOD) % MOD
            
        return total_sum