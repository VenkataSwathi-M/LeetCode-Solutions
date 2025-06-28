class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lis = nums1 + nums2
        lis.sort()
        if len(lis) % 2 == 1:
            x = int(len(lis) / 2)
            z = float(lis[x])
            return z
        else:
            x = int(len(lis) / 2)
            z = (float(lis[x-1]) + lis[x]) / 2
            return z
solu = Solution()
print(solu.findMedianSortedArrays([1,2],[3,4]))
