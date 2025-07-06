class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        lis = list(s)
        st = ""
        un = ""
        while lis:
            if i%2 == 0:
                un = ''.join(sorted(set(lis)))
                st = st + un
                for j in un:
                    lis.remove(j)
                i += 1
            elif i%2 == 1:
                un = ''.join(sorted(set(lis), reverse = True))
                st = st + un
                for j in un:
                    lis.remove(j)
                i += 1
        return st
solu = Solution()
print(solu.sortString("rat"))
