class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        """
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)
        lis1 = list()
        for i in range(0,red):
            lis1.append(0)
        for i in range(0,white):
            lis1.append(1)
        for i in range(0,blue):
            lis1.append(2)
        for i in range(0,len(lis1)):
            nums[i] = lis1[i]
        return nums
solu = Solution()
print(solu.sortColors([1,0,2]))
