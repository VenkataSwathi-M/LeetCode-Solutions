# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        curr.next = head
        k = k % length
        k1 = length - k
        new_tail = curr
        for _ in range(k1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head

            
