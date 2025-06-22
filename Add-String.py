class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        x = int(num1)
        y = int(num2)
        nums = x + y
        return str(nums)
solu =Solution()
print(solu.addStrings("123","9"))
