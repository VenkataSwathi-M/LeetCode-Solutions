class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        [5,3,4,2,8,6,7,1,3]
        """
        sor = sorted(set(arr))
        rank = {val : i+1 for i, val in enumerate(sor)}
        return [rank[num] for num in arr]
solu = Solution()
print(solu.arrayRankTransform([40,30,20,10]))
                
                
