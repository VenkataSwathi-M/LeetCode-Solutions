class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        x = 0
        lis = list()
        arr1.sort()
        for i in arr2:
            x = arr1.count(i)
            while x:
                lis.append(i)
                arr1.remove(i)
                x -= 1
        i = 0
        lis = lis + arr1
        return lis
solu = Solution()
print(solu.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))
