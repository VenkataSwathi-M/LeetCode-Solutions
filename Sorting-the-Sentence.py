class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        s = s.split()
        for i in s:
            x = i[-1]
            i = i[:-1]
            dic[x] = i
        y = 2
        wo = dic["1"]
        while y < len(s)+1:
            a = str(y)
            wo = wo + " " + dic[a]
            y += 1
        return wo
solu = Solution()
print(solu.sortSentence("Myself2 Me1 I4 and3"))
