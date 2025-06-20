class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        prev_value = 0
        total_value = 0
        for char in reversed(s):
            if x[char] < prev_value:
                total_value -= x[char]
            else:
                total_value += x[char]
                prev_value = x[char]
        return total_value
solu = Solution()
print(solu.romanToInt("III"))
                