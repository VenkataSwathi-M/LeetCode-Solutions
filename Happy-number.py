class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 :
            if n in seen:
                return False
            seen.add(n)
            t = 0
            for i in str(n):
                t += int(i)**2
                n = t
        return True
solu = Solution()
print(solu.isHappy(2))
