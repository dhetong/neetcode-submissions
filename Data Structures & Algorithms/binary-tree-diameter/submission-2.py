# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        depth_dict = {None:0}
        diameter = 0

        while(stack):
            node = stack[-1]
            if node.left and node.left not in depth_dict:
                stack.append(node.left)
            elif node.right and node.right not in depth_dict:
                stack.append(node.right)
            else:
                node = stack.pop()
                left = depth_dict[node.left]
                right = depth_dict[node.right]
                depth_dict[node] = max(left, right) + 1
                diameter = max(left+right, diameter)
        
        return diameter
