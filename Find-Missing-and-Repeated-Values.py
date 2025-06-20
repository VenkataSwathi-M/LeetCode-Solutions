class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        j = 1
        i = 0
        lis1 = list()
        lis = [item for sublist in grid for item in sublist]
        m = len(lis) 
        while i < len(lis):
            if lis.count(lis[i]) == 2 and lis[i] not in lis1:
                lis1.append(lis[i])
                for j in range(1, m + 1):
                    if j not in lis:
                        lis1.append(j)
                        break  
            i += 1  
        return lis1
solu = Solution()
x = solu.findMissingAndRepeatedValues([[1,3],[2,2]])
print(x)