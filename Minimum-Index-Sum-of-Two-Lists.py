class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
        """
        lis = list()
        lis1 = list()
        lis2 = list()
        dic = {}
        for i in list1:
            if i in list2:
                lis.append(i)
        for i in lis:
            x = list1.index(i)
            y = list2.index(i)
            dic[i] = x+y
        n = min(dic.values())
        for key,value in dic.items():
            if value == n:
                lis2.append(key)
        return lis2
solu =Solution()
print(solu.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))
