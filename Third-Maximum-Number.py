class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = sorted(set(nums),reverse = True)
        if len(x) >= 3:
            return x[2]
        elif len(x) <= 2:
            return x[0]
solu = Solution()
print(solu.thirdMax([3,2,1]))
