class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def _init_(self, lst):
        dummy = ListNode(0)
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
    def hasCycle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        fast,slow = head,head
        while (fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
solu = Solution()
lis1 = [1,2]
l1 = solu._init_(lis1)
print(solu.hasCycle(l1))
   
        
