class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
    
        total_budget = k1 + k2
        
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
       
        if sum(diffs) <= total_budget:
            return 0
       
        max_diff = max(diffs)
        counts = [0] * (max_diff + 1)
        for d in diffs:
            counts[d] += 1
 
        for d in range(max_diff, 0, -1):
            if counts[d] > 0:
           
                can_reduce = min(total_budget, counts[d])
                
                counts[d] -= can_reduce
                counts[d - 1] += can_reduce
                total_budget -= can_reduce
             
                if total_budget == 0:
                    break
                    
        min_sum_squares = 0
        for d in range(len(counts)):
            if counts[d] > 0:
                min_sum_squares += counts[d] * (d * d)
                
        return min_sum_squares
