class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = ""
        s1 = "0" 
        if len(a) > len(b):
            for i in range(len(a) - len(b)):
                b = "0" + b
        elif len(b) > len(a):
            for i in range(len(b) - len(a)):
                a = "0" + a
        for i, j in reversed(list(zip(a, b))):
            i_int = int(i)
            j_int = int(j)
            carry_int = int(s1)
            total = i_int + j_int + carry_int
            if total == 0:
                s = "0" + s
                s1 = "0"
            elif total == 1:
                s = "1" + s
                s1 = "0"
            elif total == 2:
                s = "0" + s
                s1 = "1"
            elif total == 3:
                s = "1" + s
                s1 = "1"
        if s1 == "1":
            s = "1" + s
        return s
solu = Solution()
print(solu.addBinary("1010", "1011"))   
