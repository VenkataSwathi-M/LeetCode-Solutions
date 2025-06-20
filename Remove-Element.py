class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = list()
        nums2 = list()
        for i in nums:
            if i == val:
                nums2.append(i)
            else:
                nums1.append(i)
        for i in range(len(nums1)):
            nums[i] = nums1[i]
        return len(nums1)
nums = [0,1,2,2,3,0,4,2]
solu = Solution()
k = solu.removeElement(nums, 2)
print(k)
print(nums[:k])

        