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
def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next
    print("None")
solu = Solution()
lis1 = [1,2,3,4,5]
lis1.reverse()
l1 = solu._init_(lis1)
l2 = solu.reverseList(l1)
print_linked_list(l2)

        
