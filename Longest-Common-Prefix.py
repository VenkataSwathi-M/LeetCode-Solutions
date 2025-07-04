class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        st2 = strs[0]
        i = 0
        j = 0
        k = 0
        while i < len(strs[0]):
            st = strs[0][k]
            j = 0
            k += 1
            while j < len(strs):
                if i >= len(strs[j]) or st != strs[j][i]:
                    return st2[:k-1]
                j += 1
            i += 1
        return st2[:k]
solu = Solution()
print(solu.longestCommonPrefix(["", ""])) 
