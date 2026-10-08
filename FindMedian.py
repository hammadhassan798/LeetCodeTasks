import numpy as nmaa
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
result=nmaa.median(list1)
print(result)



#manual logic will be first arrange both arrays into single array then apply formula 

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        
        i = 0
        j = 0

        merged = []

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

       
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

       
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

      
        n = len(merged)

        if n % 2 == 1:
            return float(merged[n // 2])

        else:
            middle1 = merged[n // 2 - 1]
            middle2 = merged[n // 2]

            return (middle1 + middle2) / 2.0