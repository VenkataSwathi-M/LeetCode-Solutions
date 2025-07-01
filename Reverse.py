class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        st = list()
        st = s[:]
        i = 0
        j = len(s)
        while i < len(s):
            j -= 1
            s[i] = st[j]
            i += 1
solu = Solution()
print(solu.reverseString(["h","e","l","l","o"]))
