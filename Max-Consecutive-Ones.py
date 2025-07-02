class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        nums = [1,1,0,1,1,1]
        """
        j = 1
        lis = list()
        lis1 = list()
        lis2 = list()
        if 1 not in nums:
            return 0
        for i in nums:
            if i != 1:
                j +=1
            else:
                lis.append(j)
        for i in lis:
            if i not in lis1:
                lis1.append(i)
        for i in lis1:
            lis2.append(lis.count(i))
        return max(lis2)
solu = Solution()
print(solu.findMaxConsecutiveOnes([0]))
