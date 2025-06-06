# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        current = head
        while current != None and current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

