class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        """
        if not digits:
            return []
        dis = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = ['']  
        for char in digits:
            i = []
            for char1 in result:
                for x in dis[char]:
                    i.append(char1 + x)
            result = i  
        return result
solu = Solution()
print(solu.letterCombinations("23"))
