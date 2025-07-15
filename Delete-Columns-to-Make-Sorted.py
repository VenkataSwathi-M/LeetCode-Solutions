class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        for i in zip(*strs):
            if list(i) != sorted(i):
                count += 1
        return count
solu =Solution()
print(solu.minDeletionSize(["cba","daf","ghi"]))
