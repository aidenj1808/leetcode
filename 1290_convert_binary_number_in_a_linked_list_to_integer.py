# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ret = ""
        curr = head
        while curr:
            ret += str(curr.val)
            curr = curr.next
        return int(ret, 2)

