class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Example: [-2,1,-3,4,-1,2,1,-5,4]
        """
        res = nums[0]
        maxEnd = nums[0]
        for i in range(1,len(nums)):
            maxEnd = max(maxEnd + nums[i],nums[i])
            res = max(maxEnd,res)
        return res
solu = Solution()
print(solu.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
