class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lis1 = list()
        lis2 = list()
        lis3 = list()
        for i in nums1:
            if i not in lis1:
                lis1.append(i)
        for i in nums2:
            if i not in lis2:
                lis2.append(i)
        for i in lis1:
            if i in lis2:
                lis3.append(i)
        return lis3
solu = Solution()
print(solu.intersection([4,9,5],[9,4,9,8,4]))
