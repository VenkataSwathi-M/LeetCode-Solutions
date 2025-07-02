class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        full = set(range(1, n + 1))
        return list(full - set(nums))


''' class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        m = max(nums)
        i = 1
        lis = list()
        lis1 = list()
        while i <= m:
            lis1.append(i)
            i +=1
        i = 0
        while i <= m-1:
            if lis1[i] not in nums:
                lis.append(lis1[i])
            i += 1
        if len(lis1) < len(nums):
            for i in range(len(lis1)+1,len(nums)+1):
                lis.append(i)
        return lis
solu = Solution()
print(solu.findDisappearedNumbers([1,1]))'''
