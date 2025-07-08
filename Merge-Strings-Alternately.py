class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s = ""
        if len(word1) == len(word2):
            for i,j in zip(word1,word2):
                s = s + i + j
        elif len(word1) < len(word2):
            s1 = word2[:len(word1)]
            for i,j in zip(word1,s1):
                s = s + i + j
            s = s + word2[len(word1):]
        elif len(word1) > len(word2):
            s1 = word1[:len(word2)]
            for i,j in zip(s1,word2):
                s = s + i + j
            s = s + word1[len(word2):]    
        return s
solu = Solution()
print(solu.mergeAlternately("abcd","pq"))
