class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lis = list()
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    lis.append(i)
                    lis.append(j)
                    return lis
                j+=1
            i+=1
        return lis    
solu = Solution()
x=solu.twoSum([11,7,2,3],9)
print(x)
        