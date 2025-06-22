class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num = list()
        for i in nums:
            if i in num:
                return True
                break
            else:
                num.append(i)
        return False
solu = Solution()
print(solu.containsDuplicate([1,2,1,3]))
