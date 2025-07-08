class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        2
        """
        lis = list(set(allowed))
        lis.sort()
        lis1 = list()
        x = 0
        a = list()
        for i in words:
            lis1 = list(set(i))
            lis1.sort()
            del a
            a = list()
            for i in lis1:
                if i in lis:
                    a.append(True)
                else:
                    a.append(False)
            if a.count(False) == 0:
                x +=1
        return x
solu = Solution()
print(solu.countConsistentStrings("cad",["cc","acd","b","ba","bac","bad","ac","d"]))
