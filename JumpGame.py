class Solution(object):
    def maxValue(self, nums):
        n = len(nums)

        list1 = nums[:]

        changed = True

        while changed:
            changed = False

            for i in range(n):
                for k in range(n):

                    if k > i and nums[k] < nums[i]:
                        if list1[k] > list1[i]:
                            list1[i] = list1[k]
                            changed = True

                    elif k < i and nums[k] > nums[i]:
                        if list1[k] > list1[i]:
                            list1[i] = list1[k]
                            changed = True

        return list1