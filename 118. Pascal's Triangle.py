class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            row = [1]
            if triangle:
                last_row = triangle[-1]
                row += [sum(pair) for pair in zip(last_row, last_row[1:])]
                row.append(1)
            triangle.append(row)
        return triangle
solu = Solution()
numRows = 5
for row in solu.generate(numRows):
    print(row)
