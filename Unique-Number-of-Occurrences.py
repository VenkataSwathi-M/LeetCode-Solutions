class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        x = set(arr)
        lis = list()
        lis1 = list()
        for i in x:
            c = arr.count(i)
            if c not in lis:
                lis.append(c)
                lis1.append(True)
            else:
                lis1.append(False)
        if False in lis1:
            return False
        else:
            return True
solu = Solution()
print(solu.uniqueOccurrences([1,2,2,2,1,1,3]))
                
                
