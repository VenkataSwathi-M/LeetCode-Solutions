class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = list(s)
        x= 0
        while x < len(r):
            if r[x].isdigit():
                if x > 0:
                    del r[x]  
                    del r[x-1] 
                    x -= 1    
                else:
                    del r[x]   
            else:
                x += 1
        s = "".join(r)
        return s
solu = Solution()
result = solu.clearDigits("abc")
print(result)