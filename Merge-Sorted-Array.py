class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i =0
        nums = nums1[:m] + nums2[:n]
        while i < len(nums):
            nums1[i] = nums[i]
            i +=1
        nums1.sort()
        return nums1
solu = Solution()
print(solu.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
