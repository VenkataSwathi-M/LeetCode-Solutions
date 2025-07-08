class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lis = s.split()
        s = ' '.join(lis[:k])
        return s
solu = Solution()
print(solu.truncateSentence("Hello how are you Contestant",4))
