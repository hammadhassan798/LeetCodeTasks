class Solution(object):
    def smallestUniqueSubarray(self, nums):
     
        n = len(nums)
        base = 100003
        mod = 2305843009213693951

        pows = [1] * (n + 1)
        for i in range(1, n + 1):
            pows[i] = (pows[i - 1] * base) % mod

        left = 1
        right = n
        ans = n

        while left <= right:
            size = (left + right) // 2
            toppow = pows[size - 1]

            curhash = 0
            for i in range(size):
                curhash = (curhash * base + nums[i]) % mod

            counts = {}
            counts[curhash] = 1

            for i in range(1, n - size + 1):
                outval = (nums[i - 1] * toppow) % mod
                curhash = (curhash - outval) % mod
                curhash = (curhash * base + nums[i + size - 1]) % mod
                counts[curhash] = counts.get(curhash, 0) + 1

            found = False
            for h in counts:
                if counts[h] == 1:
                    found = True
                    break

            if found:
                ans = size
                right = size - 1
            else:
                left = size + 1

        return ans
p=Solution()
print(p.smallestUniqueSubarray([3,3,3]))