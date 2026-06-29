# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head and head.next and head.next.next:
            if head.next != head.next.next:
                head = head.next
                head.next = head.next.next
            else:
                return True
        return False