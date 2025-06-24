class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        lis1 = list()
        lis2 = list()
        for i in num1:
            lis1.append(i)
        for j in num2:
             lis2.append(j)    
        x = int(''.join(lis1))
        y = int(''.join(lis2))
        return str(x*y)
solu = Solution()
print(solu.multiply("123", "456"))
