class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if (len(nums1) > len(nums2)):
            temp = nums1
            nums1 = nums2
            nums2 = temp            

        len1 = len(nums1)
        len2 = len(nums2)

        # we want nums1 to be shorter, so we can binary search it and its faster

        total = len1 + len2

        # len of the left side (the smaller elements)
        left = (len1 + len2 + 1) // 2

        low = 0
        high = len1

        while low <= high:
            mid1 = (low + high) // 2

            # items on the left of arr2, bc 'left' signifies the length of the left side of the merged array
            mid2 = left - mid1

            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

            if mid1 < len1:
                r1 = nums1[mid1]
            if mid2 < len2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 1:
                    return float(max(l1, l2))

                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0

            elif l1 > r2:
                high = mid1 - 1

            else:
                low = mid1 + 1

        return 0.0