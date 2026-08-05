# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        pre_idx = 1
        in_idx = 0
        while pre_idx < len(preorder):
            value = preorder[pre_idx]
            pre_idx += 1
            node = stack[-1]
            if node.val != inorder[in_idx]:
                node.left = TreeNode(value)
                stack.append(node.left)
            else:
                while(stack and in_idx < len(inorder) and stack[-1].val == inorder[in_idx]):
                    node = stack.pop()
                    in_idx += 1
                node.right = TreeNode(value)
                stack.append(node.right)
        return root
                