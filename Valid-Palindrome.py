class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = ""
        st1 = ""
        i = len(s)-1
        while i >= 0:
            if s[i].isalpha()  or s[i].isdigit():
                st = st + s[i]
            i -= 1
        st = st.lower()
        print(st)
        i = 0 
        while i <= len(s)-1:
            if s[i].isalpha()  or s[i].isdigit():
                st1 = st1 + s[i]
            i += 1
        st1 = st1.lower()     
        print(st1)
        if st == st1:
            return True
        return False
solu = Solution()
print(solu.isPalindrome("race a car"))
