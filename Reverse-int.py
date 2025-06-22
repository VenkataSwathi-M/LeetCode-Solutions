class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        lis = list(str(x))
        z = []
        if lis[0] == '-' or lis[0] == '+':
            z.append(lis[0])
            lis = lis[1:]
        while lis and lis[-1] == '0':
            lis.pop()
        lis.reverse()
        if z:
            lis.insert(0, z[0])
        number_str = ''.join(lis)
        if number_str == '' or number_str in ('-', '+'):
            return 0
        result = int(number_str)
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
solu = Solution()
print(solu.reverse(-2147483648))  
