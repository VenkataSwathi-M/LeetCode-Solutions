class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        dic = {}
        
        for i,j in zip(s,indices):
            dic[j] = i
        z = 0
        s = ""
        while z < len(dic):
            s = s + dic[z]
            z += 1
        return s
solu = Solution()
print(solu.restoreString("abc",[0,1,2]))
