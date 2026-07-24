"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        point = head
        copy_node_list = []
        address_dict = {}
        while point:
            copy_node = Node(point.val)
            copy_node_list.append(copy_node)
            address_dict[point] = copy_node
            point = point.next
        point = head
        for i in range(len(copy_node_list)-1):
            copy_node_list[i].next = copy_node_list[i+1]
            if point.random != None:
                copy_node_list[i].random = address_dict[point.random]
            else:
                copy_node_list[i].random = None
            point = point.next
        copy_node_list[len(copy_node_list)-1].next = None
        if point.random != None:
            copy_node_list[len(copy_node_list)-1].random = address_dict[point.random]
        else:
            copy_node_list[len(copy_node_list)-1].random = None
        return copy_node_list[0]