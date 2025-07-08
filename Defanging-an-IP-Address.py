class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        "1[.]1[.]1[.]1"
        """
        s = ""
        for i in address:
            if i == ".":
                s = s+"["+i+"]"
            else:
                s = s + i
        return s
solu = Solution()
print(solu.defangIPaddr("255.100.50.0"))
