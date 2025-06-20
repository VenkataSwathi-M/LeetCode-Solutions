class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) == 1:
                x = i
        return x
solu = Solution()
print(solu.singleNumber([4,1,2,1,2]))