# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        sum_dict = {}
        max_sum = float('-inf')
        while stack:
            node = stack[-1]
            if node.left and node.left not in sum_dict:
                stack.append(node.left)
            elif node.right and node.right not in sum_dict:
                stack.append(node.right)
            else:
                left = max(sum_dict.get(node.left, 0), 0)
                right = max(sum_dict.get(node.right, 0), 0)
                sum_dict[node] = node.val + max(left, right)
                max_sum = max(max_sum, left + right + node.val)
                stack.pop()
        return max_sum
                