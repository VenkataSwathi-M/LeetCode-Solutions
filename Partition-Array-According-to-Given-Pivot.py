class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = list() 
        greater = list()
        equ = list()
        
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            elif i == pivot:
                equ.append(i)
        return less + equ + greater
solu = Solution()
x = solu.pivotArray([-3,4,3,2],2)
print(x)
