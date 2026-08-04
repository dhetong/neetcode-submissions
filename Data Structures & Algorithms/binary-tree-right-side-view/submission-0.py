# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([(root, 1)])
        height_dict = defaultdict(list)
        while queue:
            node, height = queue.popleft()
            height_dict[height].append(node.val)
            if node.left:
                queue.append((node.left, height+1))
            if node.right:
                queue.append((node.right, height+1))
        res = []
        for h in height_dict:
            res.append(height_dict[h][-1])
        return res