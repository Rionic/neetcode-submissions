class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        preMap = defaultdict(set)
        order = []

        for crs, pre in prerequisites:
            indegree[crs] += 1
            preMap[pre].add(crs)

        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            crs = q.popleft()
            order.append(crs)
            for unlocked in preMap[crs]:
                indegree[unlocked] -= 1
                if indegree[unlocked] == 0:
                    q.append(unlocked)
        
        return order if len(order) == numCourses else []