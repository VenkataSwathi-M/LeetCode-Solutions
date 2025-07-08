class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        lis = sentence.split()
        for i in lis:
            s = ''.join(i)
            if len(searchWord) <= len(s):
                x = len(searchWord)
                if searchWord == s[:x]:
                    return lis.index(i)+1
        return -1
solu = Solution()
print(solu.isPrefixOfWord("love errichto jonathan dumb","dumb"))
