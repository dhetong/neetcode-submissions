# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        height_dict = {None:0}
        while stack:
            node = stack[-1]
            if node.left and node.left not in height_dict:
                stack.append(node.left)
            elif node.right and node.right not in height_dict:
                stack.append(node.right)
            else:
                node = stack.pop()
                left = height_dict[node.left]
                right = height_dict[node.right]
                if abs(left-right) > 1:
                    return False
                height_dict[node] = max(left,right) + 1
        return True