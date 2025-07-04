class Solution(object):
  def sqrt(self,x):
    if x == 0:
      return 0
    g = float(x)
    for _ in range(20):
      g = (g+x/g)/2.0
    return g
solu = Solution()
print(solu.sqrt(8))
