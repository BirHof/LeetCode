# 4. Median of Two Sorted Arrays
# https://www.youtube.com/watch?v=q6IEA26hvXc&t=39s&ab_channel=NeetCode

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        L1 = len(nums1)
        L2 = len(nums2)
        L3 = L1+L2
        i1 = 0
        i2 = 0
        i3 = 0
        arr3 = [0]*L3

        while i1 < L1 and i2 < L2:
            if nums1[i1] < nums2[i2]:
                arr3[i3] = nums1[i1]
                i3 += 1
                i1 += 1
            else:
                arr3[i3] = nums2[i2]
                i3 += 1
                i2 += 1
        while i1 < L1:
            arr3[i3] = nums1[i1]
            i3 += 1
            i1 += 1
        while i2 < L2:
            arr3[i3] = nums2[i2]
            i3 += 1
            i2 += 1

        if L3 % 2 == 0:
            mid_low = L3 // 2 - 1
            median = (arr3[mid_low] + arr3[mid_low+1]) / 2
        else:
            mid = L3//2 + 1 - 1
            median = arr3[mid]

        return median


nums1 = [1, 3, 4, 6, 8, 9]
nums2 = [2, 5, 7]


# nums1 = [1, 3]
# nums2 = [2]
#Output: 2.00000

nums1 = [1, 2]
nums2 = [3, 4]
#Output: 2.50000

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

obj1 = Solution()
print(obj1.findMedianSortedArrays(nums1, nums2))
