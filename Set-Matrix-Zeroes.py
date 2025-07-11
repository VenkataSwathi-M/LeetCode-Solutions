class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        """
        x1 = 0
        lis1 = list()
        lis2 = list()
        for i in matrix:
            j = 0
            while j < len(i):
                del lis1[:]
                if i[j] == 0:
                    lis1.append(x1)
                    lis1.append(j)
                    lis2.append(lis1[:])
                j += 1
            x1 += 1
        for i in lis2:
            matrix[i[0]] = [0] * len(matrix[i[0]])
            j = 0
            while j < len(matrix):
                matrix[j][i[1]] = 0 
                j += 1
        print(matrix)
solu = Solution()
print(solu.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
