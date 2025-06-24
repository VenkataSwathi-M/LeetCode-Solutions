class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        nums = [1,1,1,2,2,3]
        Output: 5, nums = [1,1,2,2,3,_]
        """
        lis1 = list()
        lis2 = list()
        num2 = list()
        z = 0
        k = 0
        for i in range(0,len(nums)):
            if nums[i] not in lis1:
                lis1.append(nums[i])
        for i in lis1:
            lis2.append(nums.count(i))
        x = max(lis2)
        if x == 1:
            k = len(lis1)
            return k
        for i in range(0,len(lis2)):
            if lis2[i] > 2:
                lis2[i] = 2
        for i in lis2:
            y = i
            for j in range(0,y):
                num2.append(lis1[z])
                k +=1
            z += 1
        for i in range(len(num2)):
            if i < len(nums):
                nums[i] = num2[i]
            else:
                nums.append(num2[i])
        return k
solu = Solution()
x = solu.removeDuplicates([0,0,1,1,1,1,2,2,2,4])
print(x)
