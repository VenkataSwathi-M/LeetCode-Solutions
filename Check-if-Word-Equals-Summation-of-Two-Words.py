class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        s = ""
        s1 = ""
        s2 = ""
        dic = {chr(97 + i) : i for i in range(26)}
        for i in firstWord:
             s = s + str(dic[i])
        for j in secondWord:
             s1 = s1 + str(dic[j])
        for z in targetWord:
            s2 = s2 + str(dic[z])
        s = int(s)
        s1 = int(s1)
        s2 = int(s2)
        if s+s1 == s2:
            return True
        else:
            return False
solu = Solution()
print(solu.isSumEqual("aaa", "a", "aaaa"))
