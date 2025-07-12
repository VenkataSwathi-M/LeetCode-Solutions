class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num1 = num
        x = 0
        while num >= 10:
            x = 0
            for i in str(num1):
                x += int(i)
                num1 = x
            num = num1
        return num
solu = Solution()
print(solu.addDigits(0))
            
        
