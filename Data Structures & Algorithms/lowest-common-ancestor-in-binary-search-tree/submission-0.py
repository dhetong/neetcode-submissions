# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [(root, [root])]
        p_flag = False
        q_flag = False
        p_path = []
        q_path = []
        while stack:
            node, path = stack.pop()
            if node == p:
                p_path = path
                p_flag = True
            if node == q:
                q_path = path
                q_flag = True
            if q_flag and p_flag:
                break
            if node.left:
                left_path = path + [node.left]
                stack.append((node.left, left_path))
            if node.right:
                right_path = path + [node.right]
                stack.append((node.right, right_path))
        index = 0
        for i in range(len(p_path)):
            print(p_path[i].val)
        for i in range(len(q_path)):
            print(q_path[i].val)
        while index < len(p_path) and index < len(q_path):
            if p_path[index] != q_path[index]:
                break
            index += 1
        return p_path[index-1]