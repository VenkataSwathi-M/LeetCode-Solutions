class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return res
sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))
