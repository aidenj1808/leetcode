import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        current = head
        while current.next:
            gcd = math.gcd(current.val, current.next.val)
            new_node = ListNode(gcd, current.next)
            current.next = new_node
            current = current.next.next
        return head
        
