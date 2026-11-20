class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()
        chain = {}
        ans = 0

        for num in nums:
            up = num + 1
            prevup = chain.get(up - 1, 0)
            curup = chain.get(up, 0)
            if prevup + 1 > curup:
                chain[up] = prevup + 1
            if chain[up] > ans:
                ans = chain[up]

            prevcur = chain.get(num - 1, 0)
            curval = chain.get(num, 0)
            if prevcur + 1 > curval:
                chain[num] = prevcur + 1
            if chain[num] > ans:
                ans = chain[num]

        return ans
p=Solution()
print(p.maxSelectedElements([2,1,5,1,1]))