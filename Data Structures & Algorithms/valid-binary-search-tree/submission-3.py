# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -1001, 1001)]
        while stack:
            node, min_number, max_number = stack.pop()
            if node.val <= min_number or node.val >= max_number:
                return False
            if node.left:
                stack.append((node.left, min_number, node.val))
            if node.right:
                stack.append((node.right, node.val, max_number))
        return True
