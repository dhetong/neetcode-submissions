# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_feature(self, root):
        stack = [root]
        features = []
        while stack:
            node = stack.pop()
            if node is None:
                features.append("-1")
                continue
            features.append('#' + str(node.val))
            # stack.append(node.right)
            # stack.append(node.left)
            stack.append(node.left)
            stack.append(node.right)
        result = "$".join(features)
        return result

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub_feature = self.get_feature(subRoot)
        feature = self.get_feature(root)

        if sub_feature in feature:
            return True
        return False