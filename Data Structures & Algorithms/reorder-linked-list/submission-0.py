# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        point = head
        node_list = []
        while point:
            node_list.append(point)
            point = point.next
        n = len(node_list)
        point = node_list[0]
        for i in range(1,n//2+1):
            if i != n-i:
                point.next = node_list[n-i]
                point = point.next
                point.next = node_list[i]
                point = point.next
                point.next = None
            else:
                point.next = node_list[i]
                point = point.next
                point.next = None