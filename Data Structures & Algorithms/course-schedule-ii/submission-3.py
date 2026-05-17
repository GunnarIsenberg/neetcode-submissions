class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqs = {i : [] for i in range(numCourses)}
        for course, req in prerequisites:
            reqs[course].append(req)
        
        visited, cycle = set(), set()
        res = []

        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            
            cycle.add(node)
            for req in reqs[node]:
                if not dfs(req):
                    return False
            cycle.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        