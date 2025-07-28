class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        weight_map = defaultdict(int)
        for values, weight in items1:
            weight_map[values] += weight
        for values, weight in items2:
            weight_map[values] += weight
        merge = [[values,weight] for values,weight in weight_map.items()]
        merge.sort()
        return merge
solu = Solution()
print(solu.mergeSimilarItems(items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]))
