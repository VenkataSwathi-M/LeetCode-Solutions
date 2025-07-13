class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        "AceCreIm"
        """
        l =['a', 'e', 'i', 'o', 'u']
        lis1 = list()
        lis2 = list()
        lis3 = list(s)
        for index, value in enumerate(s):
            if value.lower() in l:
                lis1.append(value)
                lis2.append(index)
        lis1.reverse()
        for index, value in zip(lis2,lis1):
            lis3[index] = value
        s = ''.join(lis3)
        return s
solu = Solution()
print(solu.reverseVowels("leetcode"))
