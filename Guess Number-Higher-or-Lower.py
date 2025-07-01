pick = 6  
def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0
class Solution(object):
    def guessNumber(self, n):
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                low = mid + 1
            else:
                high = mid - 1
solu = Solution()
print(solu.guessNumber(10)) 
