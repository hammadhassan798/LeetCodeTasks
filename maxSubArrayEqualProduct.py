class Solution(object):
    def maxLength(self, nums):
        n = len(nums)
        maxlen = 0

        for i in range(n):
            curprod = 1
            curgcd = 0
            curlcm = 1

            for j in range(i, n):
                val = nums[j]
                curprod = curprod * val

                if curgcd == 0:
                    curgcd = val
                else:
                    tempa = curgcd
                    tempb = val
                    while tempb != 0:
                        rem = tempa % tempb
                        tempa = tempb
                        tempb = rem
                    curgcd = tempa

                tempa = curlcm
                tempb = val
                while tempb != 0:
                    rem = tempa % tempb
                    tempa = tempb
                    tempb = rem
                pairgcd = tempa
                curlcm = (curlcm // pairgcd) * val

                if curprod == curlcm * curgcd:
                    curlen = j - i + 1
                    if curlen > maxlen:
                        maxlen = curlen

        return maxlen
p=Solution()
print(p.maxLength([1,2,1,2,1,1,1]))