class ListNode(object):
    def init(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def list_to_linked_list(self, lst):
        dummy = ListNode(0)
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next  
def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next
    print("None")
solu = Solution()
l1 = solu.list_to_linked_list([1, 2, 4])
l2 = solu.list_to_linked_list([1, 3, 4])
merged = solu.mergeTwoLists(l1, l2)
print_linked_list(merged)
