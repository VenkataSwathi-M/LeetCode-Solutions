class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        lis = text.split()
        lis1 = list()
        x = 0
        for i in lis:
            if x == len(lis)-2:
                break
            if lis[x] == first and lis[x+1] == second:
                lis1.append(lis[x+2])
            x += 1
        return lis1
solu = Solution()
print(solu.findOcurrences("we will we will rock you", "we", "will"))
