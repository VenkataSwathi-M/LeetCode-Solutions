class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp0 = 0
        temp1 = 0
        arr = list()
        for x in range(len(nums)-1):
            temp0 = nums[x]
            temp1 = nums[x+1]
            if (temp0 % 2 == 0 and temp1 % 2 ==1) or (temp0 % 2 == 1 and temp1 % 2 ==0):
                arr.append(True)
            else:
                arr.append(False)
        if False in arr:
            return False
        else:
            return True
solu = Solution()
nums = [4,3,1,6]
solu.isArraySpecial(nums)
