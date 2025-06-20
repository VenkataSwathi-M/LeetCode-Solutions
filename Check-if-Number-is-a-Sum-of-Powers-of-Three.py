class Solution(object):
    def checkPowersOfThree(self,n):
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
solu = Solution()
x = solu.checkPowersOfThree(27)
print(x)
            
        