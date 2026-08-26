class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        l = len(beginWord)
        unvisited = set(wordList)
        def check(w1, w2):
            count = 0
            for i in range(l):
                if w1[i] != w2[i]:
                    count += 1
            return count == 1
        queue = deque([(beginWord, 1)])
        while queue:
            current, step = queue.popleft()
            if current == endWord:
                return step
            for word in list(unvisited):
                if check(word, current):
                    unvisited.remove(word)
                    queue.append((word, step + 1))
        return 0