class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        words = ["Hello","Alaska","Dad","Peace"]
        """
        f = list("qwertyuiop")
        s = list("asdfghjkl")
        t = list("zxcvbnm")
        lis = list()
        lis1 = list()
        for i in words:
            s1 = list(i)
            del lis[:]     
            for j in s1:
                j = j.lower()
                if j in f:
                    lis.append(1)
                elif j in s:
                    lis.append(2)
                elif j in t:
                    lis.append(3)
            lis1.append(list(lis))
        del lis[:]     
        for idx, sublist in enumerate(lis1):
            if len(set(sublist)) == 1:
                lis.append(words[idx])
        return lis         
solu = Solution()
print(solu.findWords(["adsdf","sfd"]))
                
                
