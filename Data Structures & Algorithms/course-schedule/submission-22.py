class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Prereq -> courses it unlocks
        preMap = defaultdict(list)

        # Indegree = prereqs remaining
        indegree = [0 for _ in range(numCourses)]

        for crs, pre in prerequisites:
            indegree[crs] += 1
            preMap[pre].append(crs)

        taken = 0
        q = deque()
        for crs in range(len(indegree)):
            if indegree[crs] == 0:
                q.append(crs)

        while q:
            pre = q.popleft()
            taken += 1
            for crs in preMap[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        
        return taken == numCourses


        