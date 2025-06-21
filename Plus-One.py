class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(map(str, digits)))
        num += 1 
        digit = [int(d) for d in str(num)]
        return digit
solu = Solution()
print(solu.plusOne([4,3,2,2]))
        
