class Solution(object):
    def smallestUniqueSubarray(self, nums):

        n = len(nums)

        for size in range(1, n + 1):
            slices = []

            for i in range(n - size + 1):
                piece = nums[i:i + size]
                slices.append(piece)

            for piece in slices:
                if slices.count(piece) == 1:
                    return size

        return n
p=Solution()
print(p.smallestUniqueSubarray([3,3,3]))