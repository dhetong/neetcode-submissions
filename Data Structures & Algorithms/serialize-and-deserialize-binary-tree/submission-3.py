# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        features = []
        while queue:
            node = queue.popleft()
            if node == None:
                features.append('N')
            else:
                features.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return '#'.join(features)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == 'N':
            return None
        features = data.split('#')
        root = TreeNode(int(features[0]))
        queue = deque([root])
        assign_child = 0
        parent = queue.popleft()
        for feature in features[1:len(features)]:
            if assign_child == 2:
                parent = queue.popleft()
                assign_child = 0
            if feature == 'N':
                pass
            else:
                node = TreeNode(int(feature))
                if assign_child == 0:
                    parent.left = node
                else:
                    parent.right = node
                queue.append(node)
            assign_child += 1
        return root