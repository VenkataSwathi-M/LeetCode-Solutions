class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,1,1,2,1,2]
        """
        lis = list()
        lis1 = list()
        for i in nums:
            if i not in lis:
                lis.append(i)
                lis1.append(nums.count(i))
        m = max(lis1)
        n = lis1.index(m)
        return lis[n]
solu = Solution()
print(solu.majorityElement([1,1,1,2,1,2]))
        
            
        
        
