# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []
        point = head
        while point:
            node_list.append(point)
            point = point.next
        total = len(node_list)
        target = total - n
        if target == 0:
            head = head.next
        else:
            if target + 1 < total:
                node_list[target-1].next = node_list[target+1]
            else:
                node_list[target-1].next = None
        return head