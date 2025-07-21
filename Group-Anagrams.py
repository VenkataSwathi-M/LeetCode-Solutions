from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        [["bat"],["nat","tan"],["ate","eat","tea"]]
        """
        anagrams = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            anagrams[key].append(i)
        return list(anagrams.values())
solu = Solution()
x = solu.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(x)

            
                    
                        
