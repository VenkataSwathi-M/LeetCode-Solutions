class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis = s.split()
        return len(lis)
solu = Solution()
print(solu.countSegments("Hello, my name is John"))
