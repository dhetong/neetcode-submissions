# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_depth(self, root):
        if not root:
            return 0
        stack = [(root,1)]
        max_depth = 1
        while stack:
            node_info = stack.pop()
            node = node_info[0]
            depth = node_info[1]
            max_depth = max(depth, max_depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return max_depth

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        diameter = 0
        while stack:
            node = stack.pop()
            left = self.get_depth(node.left)
            right = self.get_depth(node.right)
            diameter = max(diameter, left+right)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return diameter
