# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = False
        head = None
        point = None
        while l1 and l2:
            val = l1.val + l2.val
            if flag:
                val += 1
            if val >= 10:
                flag = True
            else:
                flag = False
            val = val % 10
            if head == None:
                head = ListNode(val)
                point = head
            else:
                tmp = ListNode(val)
                point.next = tmp
                point = tmp
            l1 = l1.next
            l2 = l2.next
        rest_point = l1 or l2
        while rest_point:
            val = rest_point.val
            if flag:
                val += 1
            if val >= 10:
                flag = True
            else:
                flag = False
            val = val % 10
            if head == None:
                head = ListNode(val)
                point = head
            else:
                tmp = ListNode(val)
                point.next = tmp
                point = tmp
            rest_point = rest_point.next
        if flag:
            tmp = ListNode(1)
            point.next = tmp
            point = tmp
        return head