class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirst(nums, target):
            low,high = 0, len(nums) - 1
            index = -1
            lis = list()
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    index = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return index
        def findLast(nums, target):
            low,high = 0, len(nums) - 1
            index = -1
            lis = list()
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    index = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return index
        return [findFirst(nums, target), findLast(nums, target)]
solu = Solution()
print(solu.searchRange([5,7,7,8,8,10],8))
        
        
