# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        headminheap = []
        for point in lists:
            node = NodeWrapper(point)
            heapq.heappush(headminheap, node)
        
        head = ListNode(0)
        point = head
        while headminheap:
            min_head = heapq.heappop(headminheap)
            point.next = min_head.node
            point = point.next
            update_node = min_head.node.next
            if update_node:
                node = NodeWrapper(update_node)
                heapq.heappush(headminheap, node)
        return head.next