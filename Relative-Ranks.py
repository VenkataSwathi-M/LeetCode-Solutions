class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
        """
        lis = ["Gold Medal","Silver Medal","Bronze Medal"]
        dic = {}
        sorted_lis = sorted(score,reverse = True)
        lis1 = list()
        i = 4
        while i < len(score)+1:
            lis.append(str(i))
            i +=1
        for n,k in zip(sorted_lis,lis):
            dic[n] = k
        for i in score:
            lis1.append(dic[i])
        return lis1
solu =Solution()
print(solu.findRelativeRanks([5,4,3,2,1]))
