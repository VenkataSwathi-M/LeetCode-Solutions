class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        "bab"
        """
        if len(s) == 1:
            return s
        j = len(s)-1
        i = 0 
        temp = ""
        m = 0
        l = 0
        while i < len(s):
            j = len(s)-1
            while j > 0 :
                if i == j:
                    break
                elif s[i] == s[j]:
                    r = s[i:j+1]
                    if r == r[::-1]:
                        m = len(r)
                        if m > l:
                            temp = r
                            l = len(temp)
                j -= 1
            i += 1
        if len(temp) == 0:
            return s[0]
        else:
            return temp
solu = Solution()
print(solu.longestPalindrome("aacabdkacaa"))
