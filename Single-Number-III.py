class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        nums = [1,2,1,3,2,5]
        Output: [3,5]
        """
        x = list()
        for i in nums:
            if nums.count(i) == 1:
                x.append(i)
        return x
solu = Solution()
print(solu.singleNumber([1,2,1,3,2,5]))
