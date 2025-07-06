class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = list()
        lis1 = list()
        nums.sort()
        for i in nums:
            if nums.count(i) >= 2:
                lis1.append(i)
            elif nums.count(i) == 1:
                lis.append(i)
        return sum(i for i in lis)
solu = Solution()
print(solu.sumOfUnique([58,63,82,92,68,17,61,19,27,83,37,50,2,4,52,15,99,82,94,74,32,19,98,97,31,61,23,53,40,38,68,50,50,50,74,92,100]))
