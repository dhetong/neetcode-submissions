# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()
            if node_p and node_q:
                if node_p.val != node_q.val:
                    return False
            else:
                if node_p == None and node_q == None:
                    pass
                else:
                    return False
            if node_p.left and node_q.left:
                stack_p.append(node_p.left)
                stack_q.append(node_q.left)
            else:
                if node_p.left == None and node_q.left == None:
                    pass
                else:
                    return False
            if node_p.right and node_q.right:
                stack_p.append(node_p.right)
                stack_q.append(node_q.right)
            else:
                if node_p.right == None and node_q.right == None:
                    pass
                else:
                    return False
        return True