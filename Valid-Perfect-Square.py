class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 1
        high = num
        while low <= high:
            mid = (low + high)//2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                low = mid + 1
            else:
                high = mid -1
        return False
solu = Solution()
print(solu.isPerfectSquare(14))
