class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        // set(candyType) give unique number
        """
        return min(len(set(candyType)), len(candyType) // 2)
solu = Solution()
print(solu.distributeCandies([6,6,6,6]))
                
                
