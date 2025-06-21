
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = s.split()
        print(x)
        y = len(x)
        z = x[y-1]
        return len(z)
solu = Solution()
print(solu.lengthOfLastWord("   fly me   to   the moon  "))