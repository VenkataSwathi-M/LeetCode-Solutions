class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lis = {}
        lis1 = {}
        j = 0
        for i in s:
            if i not in lis:
                lis[i] = j
                j+=1
        j = 0
        for i in t:
            if i not in lis1:
                lis1[i] = j
                j+=1
        x = list()
        y = list()
        for i in s:
            x.append(lis.get(i))
        for i in t: 
            y.append(lis1.get(i))
        if x == y:
            return True
        else: 
            return False
solu = Solution()
print(solu.isIsomorphic("bbbaaaba","aaabbbba"))
