class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        point = self.root
        for c in list(word):
            if c not in point.children:
                point.children[c] = TreeNode()
            point = point.children[c]
        point.end = True
    
    def search(self, word: str) -> bool:
        point = self.root
        def dfs(node, index):
            if index == len(word):
                if node.end:
                    return True
                else:
                    return False
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            else:
                if word[index] == '.':
                    for child in node.children:
                        if dfs(node.children[child], index+1):
                            return True
                    return False
                return False
        return dfs(point, 0)