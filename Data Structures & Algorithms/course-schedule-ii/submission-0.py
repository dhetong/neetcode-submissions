class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        classmap = defaultdict(list)
        indegree = [0]*numCourses
        for child, parent in prerequisites:
            classmap[parent].append(child)
            indegree[child] += 1
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for child in classmap[c]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        if len(res) == numCourses:
            return res
        else:
            return []