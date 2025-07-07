class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        i = 0
        while i < len(s):
            y = s[0]
            x = s[1:]
            lis = x.split()
            lis.append(y)
            s = ''.join(lis)
            if s == goal:
                return True
            del lis
            i += 1
        return False
solu = Solution()
print(solu.rotateString("abcde","abced"))
