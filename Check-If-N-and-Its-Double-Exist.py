class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        i != j
        0 <= i, j < arr.length
        arr[i] == 2 * arr[j]
        """
        i = 0
        j = 1
        while i < len(arr):
            while j < len(arr):
                if i != j:
                    if arr[i] == 2 * arr[j]:
                        return True
                j += 1
            i += 1
            j = 0
        return False
solu = Solution()
print(solu.checkIfExist([-20,8,-6,-14,0,-19,14,4]))
                
                
