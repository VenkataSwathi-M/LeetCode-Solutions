class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        w1 = ''.join(word1)
        w2 = ''.join(word2)
        if w1 == w2:
            return True
        else:
            return False
solu = Solution()
print(solu.arrayStringsAreEqual(["abc", "d", "defg"],["abcddefg"]))
