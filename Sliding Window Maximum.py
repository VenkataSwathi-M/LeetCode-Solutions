from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        [3,3,5,5,6,7]
        """
        dp = deque()
        result = []
        for i in range(len(nums)):
            if dp and dp[0] < i - k + 1:
                dp.popleft()
            while dp and nums[dp[-1]]<nums[i]:
                dp.pop()
            dp.append(i)
            if i>=k-1:
                result.append(nums[dp[0]])
        return result
solu = Solution()
print(solu.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
