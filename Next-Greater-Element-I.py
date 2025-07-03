class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        j = 1
        lis = list()
        for i in nums1:
            s = nums2.index(i)
            j = 1
            if s == len(nums2)-1:
                lis.append(-1)
            while j < len(nums2[s:]):
                if nums2[s] < nums2[s+j]:
                    lis.append(nums2[s+j])
                    break
                elif j == len(nums2[s:])-1:
                    lis.append(-1) 
                j +=1
        return lis
solu = Solution()
print(solu.nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))
