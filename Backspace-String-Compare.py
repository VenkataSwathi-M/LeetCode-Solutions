class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lis = list(s)
        lis1 = list(t)
        for i in s:
            if i == "#":
                x = lis.index(i)
                if x == 0:
                    del lis[x]
                else:
                    del lis[x]
                    del lis[x-1]
        for j in t:
            if j == "#":
                y = lis1.index(j)
                if y == 0:
                    del lis1[y]
                else:
                    del lis1[y]
                    del lis1[y-1]

        if lis == lis1:
            return True
        else:
            return False
solu = Solution()
print(solu.backspaceCompare("y#fo##f","y#f#o##f"))
