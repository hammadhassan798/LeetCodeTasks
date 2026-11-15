class Solution(object):
    def numofsubarrays(self, arr):
       
        # subarr = []
        # sumarr = []
        # count = 0
        # 
        # for i in range(len(arr)):
        #     for j in range(i, len(arr)):
        #         sub = arr[i:j+1]
        #         subarr.append(sub)
        # 
        # for i in range(len(subarr)):
        #     minisum = 0
        #     for j in subarr[i]:
        #         minisum += j
        #     sumarr.append(minisum)
        #     
        # for i in sumarr:
        #     if i % 2 == 1:
        #         count += 1
        #         
        # return count % 1000000007

        # ==========================================
        # OPTIMIZED O(N) LINEAR APPROACH:
        # ==========================================
        mod = 1000000007
        result = 0
        evens = 1
        odds = 0
        currentsum = 0
        
        for num in arr:
            currentsum += num
            if currentsum % 2 == 0:
                result = (result + odds) % mod
                evens += 1
            else:
                result = (result + evens) % mod
                odds += 1
                
        return result

p = Solution()
print(p.numofsubarrays([1, 3, 5]))