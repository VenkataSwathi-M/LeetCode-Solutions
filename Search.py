class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in nums:
            if i == target:
                x = nums.index(i)
                return x
        return -1
solu = Solution()
print(solu.search([4,5,6,7,0,1,2],0))
        
