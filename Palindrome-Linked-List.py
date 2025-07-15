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
    def reverseList(self,head):
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half_head = self.reverseList(slow)
        first_half = head
        second_half = second_half_head
        result = True
        while second_half:
            if first_half.val != second_half.val:
                result = False
                break
            first_half = first_half.next
            second_half = second_half.next
        return result
solu = Solution()
lis1 = [1,2]
l1 = solu._init_(lis1)
print(solu.isPalindrome(l1))
