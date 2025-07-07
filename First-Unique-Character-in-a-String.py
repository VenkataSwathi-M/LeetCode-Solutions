class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sr = set(s)
        dic = {}
        lis = list()
        for i in sr:
            if s.count(i) < 2:
                dic[i] = s.count(i)
        for i in dic.keys():
            lis.append(s.index(i))
        if len(lis) == 0:
            return -1
        else:
            return min(lis)
solu = Solution()
print(solu.firstUniqChar("leetcode"))
