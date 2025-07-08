class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        lis = sorted(set(sentence))
        if len(lis) == 26:
            return True
        else:
            return False
solu = Solution()
print(solu.checkIfPangram("leetcode"))
