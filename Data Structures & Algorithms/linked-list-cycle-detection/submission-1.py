# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 1
        node_set = set()
        while head and head not in node_set:
            node_set.add(head)
            head = head.next
        if head:
            return True
        else:
            return False