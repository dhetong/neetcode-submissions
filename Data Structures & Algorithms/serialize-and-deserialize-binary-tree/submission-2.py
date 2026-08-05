# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        feature = ''
        stack = [root]
        while stack:
            node = stack.pop()
            if node == None:
                feature = feature + 'None' + '#'
            else:
                feature = feature + str(node.val) + '#'
                stack.append(node.right)
                stack.append(node.left)
        return feature
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == 'None#':
            return None
        node_info_list = data[0:len(data)-1].split('#')
        print(node_info_list)
        root = TreeNode(int(node_info_list[0]))
        stack = [root]
        none_child = 0
        for node_info in node_info_list[1:len(node_info_list)]:
            if node_info == 'None':
                none_child += 1
            else:
                node = TreeNode(int(node_info))
                if none_child == 0:
                    stack[-1].left = node
                    stack.append(node)
                elif none_child == 1:
                    stack[-1].right = node
                    stack.append(node)
                    none_child = 0
                else:
                    parent = stack[-1]
                    while none_child > 0 or parent.right:
                        parent = stack.pop()
                        none_child -= 1
                    parent.right = node
                    none_child = 0
                    stack.append(node)
        return root