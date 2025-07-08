class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        "abbdcfdhe"
        """
        dic = {chr(97 + i) : i for i in range(26)}
        dic1 = {i : chr(97 + i)for i in range(26)}
        s1 = ""
        x = 0
        for i in s:
            if i.isalpha():
                x = dic[i]
                s1 = s1 + i
            elif i.isdigit():
                i = int(i)
                y = dic1[x+i]
                s1 = s1 + y
        return s1
solu = Solution()
print(solu.replaceDigits("a1b2c3d4e"))
