class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        10000000
        """
        r = ""
        while n > 0:  
            n1 = n
            n = n//2
            r1 = n1 % 2
            r = str(r1) + r
        return r.count("1")
solu = Solution()
print(solu.hammingWeight(2147483645))
            
        
