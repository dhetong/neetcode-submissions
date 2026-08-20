class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        classmap = defaultdict(list)
        for child, parent in prerequisites:
            classmap[parent].append(child)
            indegree[child] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        finish = 0
        while queue:
            c = queue.popleft()
            finish += 1
            for child in classmap[c]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        return finish == numCourses