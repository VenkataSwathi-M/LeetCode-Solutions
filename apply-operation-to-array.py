class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        y = len(nums)-1
        while i < len(nums):
            if i == y:
                break
            else:
                if nums[i] == nums[i+1]:
                    x = nums[i]
                    nums[i] = x*2
                    nums[i+1] = 0
                    i+=1
                else:
                    i+=1
        i=0
        d=0
        c = nums.count(0)
        while i < len(nums):
            if d == c:
                break
            else:
                if nums[i] == 0 :
                    del nums[i]
                    nums.append(0)
                    d +=1
                    i-=1
                else:
                    i+=1
        return nums
solu = Solution()
x = solu.applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272])
print(x)
