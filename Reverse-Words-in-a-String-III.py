class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis = s.split()
        lis1 = list()
        st = ""
        i = 0
        for i in lis:
            x = ''.join(i)
            lis1.append(x[::-1])
        st = ' '.join(lis1)
        return st
solu = Solution()
print(solu.reverseWords("Mr Ding"))
