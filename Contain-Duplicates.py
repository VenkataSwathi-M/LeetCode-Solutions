class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
solu = Solution()
print(solu.containsDuplicate([1, 2, 1, 3]))
