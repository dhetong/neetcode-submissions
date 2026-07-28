# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        point = head
        while True:
            min_list = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if min_list == -1 or lists[i].val < lists[min_list].val:
                    min_list = i
            if min_list == -1:
                break
            point.next = lists[min_list]
            lists[min_list] = lists[min_list].next
            point = point.next
        return head.next