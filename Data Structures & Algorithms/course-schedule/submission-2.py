class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        classmap = defaultdict(list)
        for prerequisite in prerequisites:
            parentclass = prerequisite[1]
            childclass = prerequisite[0]
            classmap[parentclass].append(childclass)
        states = [0]*numCourses
        def dfs(c):
            if states[c] == 1:
                return False
            if states[c] == 2:
                return True
            states[c] = 1
            for child in classmap[c]:
                if not dfs(child):
                    return False
            states[c] = 2
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True