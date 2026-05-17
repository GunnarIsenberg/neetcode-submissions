class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReqs = {i : [] for i in range(numCourses)}
        res = []
        for course, preReq in prerequisites:
            preReqs[course].append(preReq)
        
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for preReq in preReqs[course]:
                if not dfs(preReq):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
        
        



        