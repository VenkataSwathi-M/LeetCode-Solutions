class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lis = {}
        lis1 = {}
        s = s.split()
        j = 0
        for i in pattern:
            if i not in lis:
                lis[i] = j
                j+=1
        j = 0
        for i in s:
            if i not in lis1:
                lis1[i] = j
                j+=1
        x = list()
        y = list()
        for i in pattern:
            x.append(lis.get(i))
        for i in s: 
            y.append(lis1.get(i))
        if x == y:
            return True
        else: 
            return False
solu = Solution()
print(solu.wordPattern("aaaa","dog cat cat fish"))
