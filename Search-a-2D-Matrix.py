class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        lis1 = [num for num1 in matrix for num in num1]
        if target in lis1:
            return True
        else:
            return False
solu = Solution()
print(solu.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
