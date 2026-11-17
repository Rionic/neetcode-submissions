class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: set() for i in range(numCourses)}
        for crs, pre in prerequisites:
            courses[crs].add(pre)
        visited = set()
        # 1: {2, 4}, 2: {3}, 3: {4}, 4: {}
        def dfs(crs):
            if crs in courses[crs]:
                return False
            if len(courses[crs]) == 0: # We can take this course
                if crs in visited:
                    visited.remove(crs)
                return True
            elif crs in visited: # Cycle -> False
                return False
            # This course is currently trying to have its prereqs satisfied
            visited.add(crs)
            
            for prereq in courses[crs]:
                if not dfs(prereq):
                    return False
            # We have taken all prereqs of this course
            courses[crs] = set()
            return True
        print(courses)
        for crs in courses:
            if len(courses[crs]) > 0 and not dfs(crs):
                return False

        return True
