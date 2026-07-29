# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        reverse_window = []
        res = ListNode(0)
        point = res

        while head:
            if len(reverse_window) < k:
                reverse_window.append(head)
                head = head.next
                continue
            for i in range(1,k):
                reverse_window[i].next = reverse_window[i-1]
            point.next = reverse_window[k-1]
            point = reverse_window[0]
            reverse_window = [head]
            head = head.next
        
        if len(reverse_window) == k:
            for i in range(1,k):
                reverse_window[i].next = reverse_window[i-1]
            point.next = reverse_window[k-1]
            point = reverse_window[0]
            point.next = None
        else:
            point.next = reverse_window[0]
        
        return res.next