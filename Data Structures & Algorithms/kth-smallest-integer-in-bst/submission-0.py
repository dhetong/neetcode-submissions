# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        index = 0
        visited_nodes = []
        while stack:
            node = stack[-1]
            if node.left and node.left not in visited_nodes:
                stack.append(node.left)
                visited_nodes.append(node.left)
            else:
                stack.pop()
                index += 1
                if index == k:
                    return node.val
                if node.right and node.right not in visited_nodes:
                    stack.append(node.right)
                    visited_nodes.append(node.right)