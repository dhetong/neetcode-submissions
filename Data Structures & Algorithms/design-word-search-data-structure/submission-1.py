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
        node_queue = deque([(self.root, 0)])
        while node_queue:
            point, index = node_queue.popleft()
            if index == len(word):
                if point.end:
                    return True
                else:
                    continue
            if word[index] in point.children:
                node_queue.append((point.children[word[index]], index+1))
            else:
                if word[index] == '.':
                    for child in point.children:
                        node_queue.append((point.children[child], index+1))
        return False