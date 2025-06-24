class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [[7,4,1],[8,5,2],[9,6,3]]
        """
        x = len(matrix)
        lis1 = list()
        lis2 = list()
        i = 0 
        j = 0
        while i < len(matrix):
            lis1 = [] 
            j = 0
            while j < len(matrix):
                x -= 1
                lis1.append(matrix[x][i])
                j +=1
            lis2.append(list(lis1))
            x = len(matrix)
            i +=1
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                matrix[i][j] = lis2[i][j]
        return  matrix
solu = Solution()
print(solu.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
        
