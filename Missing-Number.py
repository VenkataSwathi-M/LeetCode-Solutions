class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)):
            if i not in nums:
               return i 
        return i + 1
solu = Solution()
print(solu.missingNumber([0,1]))
