class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total = Counter(basket1+basket2)
        for fruit in total:
            if total[fruit]%2 != 0:
                return -1
        min_fruit = min(total.keys())
        excess = []
        for fruit in total:
            target = total[fruit] // 2
            if count1[fruit] > target:
                excess.extend([fruit] * (count1[fruit] - target))
            elif count2[fruit] > target:
                excess.extend([fruit] * (count2[fruit] - target))
        excess.sort()
        n = len(excess)
        cost = 0
        for i in range(n//2):
            cost += min(excess[i],2 * min_fruit)
        return cost
