# Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums1 += nums2
    nums1.sort()
    lon = len(nums1)
    if lon % 2 == 0:
        print((nums1[lon // 2 - 1] + nums1[lon // 2]) / 2)
    else:
        print(nums1[lon // 2])

findMedianSortedArrays([1, 3], [2, 7])
