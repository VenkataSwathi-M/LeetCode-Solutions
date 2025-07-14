# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def _init_(self,l1):
        dummy = ListNode(0)
        curr = dummy
        for value in l1:
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast,slow = head,head
        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow

def print_from_node(node):
    while node:
        print(node.val)
        node = node.next
solu = Solution()
l1 = [1,2,3,4,5]
head = solu._init_(l1)
mid = solu.middleNode(head)
print_from_node(mid)
