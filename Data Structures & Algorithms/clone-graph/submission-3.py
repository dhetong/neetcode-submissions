"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        stack = [node]
        node_addr_dict = {node:Node(node.val)}
        while stack:
            curr = stack.pop()
            copy_node = node_addr_dict[curr]
            for neighbor in curr.neighbors:
                if neighbor in node_addr_dict:
                    copy_node.neighbors.append(node_addr_dict[neighbor])
                else:
                    node_addr_dict[neighbor] = Node(neighbor.val)
                    copy_node.neighbors.append(node_addr_dict[neighbor])
                    stack.append(neighbor)
        return node_addr_dict[node]