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
        queue = deque([node])
        node_addr_dict = {}
        visited = [node.val]
        while queue:
            curr = queue.popleft()
            new_node = None
            if curr.val in node_addr_dict:
                new_node = node_addr_dict[curr.val]
            else:
                new_node = Node(curr.val)
                node_addr_dict[curr.val] = new_node
            for neighbor in curr.neighbors:
                if neighbor.val in node_addr_dict:
                    new_node.neighbors.append(node_addr_dict[neighbor.val])
                else:
                    new_neighbor = Node(neighbor.val)
                    node_addr_dict[neighbor.val] = new_neighbor
                    new_node.neighbors.append(new_neighbor)
                if neighbor.val not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor.val)
        return node_addr_dict[node.val]