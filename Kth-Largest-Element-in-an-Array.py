class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        nums.reverse()
        return nums[k-1]
solu = Solution()
print(solu.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
            
        
