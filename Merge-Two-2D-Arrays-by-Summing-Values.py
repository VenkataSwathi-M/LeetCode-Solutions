class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        nums = nums1 + nums2
        nums.sort()
        lis = list()
        x=0
        d=len(nums)-1
        while x < len(nums):
            if x+1 == len(nums):
                y = nums[d][0]
                a = nums[d][1]
                lis.append([y,a])
                break
            else:
                if nums[x][0] == nums[x+1][0]:
                    y = nums[x][0]
                    a = nums[x][1]
                    b = nums[x+1][1]
                    c = a+b
                    lis.append([y,c])
                    x +=2
                else:
                    y = nums[x][0]
                    a = nums[x][1]
                    lis.append([y,a])
                    x +=1
        return lis
solu = Solution()
x = solu.mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]])
print(x)
    
        