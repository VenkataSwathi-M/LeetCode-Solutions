class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
            i +=1
        return nums
solu = Solution()
print(solu.moveZeroes([0,0,1]))
