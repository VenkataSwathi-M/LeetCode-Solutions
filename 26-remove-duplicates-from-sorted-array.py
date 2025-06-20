class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #create a new list to store unique elements
        nums1 = []
        #iterate over each number in the input list
        for i in nums:
            #if the number is not already in nums1, add it
            if i not in nums1:
                nums1.append(i)
        #overwrite the first part of nums with the unique values
        for i in range(len(nums1)):
            nums[i] = nums1[i]
        #return the count of unique elements
        return len(nums1)
# test case
nums = [1, 1, 2]
solu = Solution()
k = solu.removeDuplicates(nums)
# Output the number of unique elements
print(k)
# Output the unique part of the modified list
print(nums[:k])
